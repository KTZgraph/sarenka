from lib2to3.pytree import Base
from pyexpat import model
from statistics import mode
from typing import List, Dict, Optional
import requests
from bs4 import BeautifulSoup
from zipfile import ZipFile
import os
import json
from apps.vulnerabilities import models
from .cve_saver import get_and_save_cve
import traceback


MAIN_URL  = "https://nvd.nist.gov/vuln/data-feeds#JSON_FEED"
BASE_URL = "https://nvd.nist.gov/"

def get_dict_from_json_file(filepath: str) -> dict:
    with open(filepath, "r", encoding='utf-8') as f:
        data = json.loads(f.read())
    return data

def get_files_url(url=MAIN_URL, base_url=BASE_URL)->List[str]:
    source = requests.get(url).text
    soup = BeautifulSoup(source, "html.parser")
    soup = soup.find("div", {"id": "divJSONFeeds"})
    soup = soup.find("table")  # tylko jedna tabela w sordku diva

    files_urls = []
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if href.split(".")[-1] == "zip":
            files_urls.append(f'{base_url}{href}')

    return files_urls
    # https://nvd.nist.gov/feeds/json/cve/1.1/nvdcve-1.1-modified.json.zip
    # https://nvd.nist.gov/feeds/json/cve/1.1/nvdcve-1.1-2022.json.zip

def download_file(file_url:str)->str:
    zip_filename = file_url.split("/")[-1]
    data = requests.get(file_url)
    with open(zip_filename, "wb") as f:
        f.write(data.content)
    with ZipFile(zip_filename, "r") as zip_ref:
        extracted_file_name = zip_ref.namelist()
        zip_ref.extractall('.')

    os.remove(zip_filename)
    return extracted_file_name[0]

def save_version_to_cve(version:str, cve_obj:models.CVE)->None:
    if version and cve_obj:
        data_version, _ = models.Version.objects.get_or_create(version=float(version))
        if cve_obj is not None and data_version:
            cve_obj.version = data_version
            cve_obj.save()

def save_assigner_to_cve(assigner_email:str, cve_obj:models.CVE)->None:
    if assigner_email:
        assigner_obj, _ = models.Assigner.objects.get_or_create(email=assigner_email)
        if cve_obj:
            cve_obj.assigner = assigner_obj
            cve_obj.save()

def save_format_to_cve(format_name:str, cve_obj:models.CVE)->None:
    if format_name and cve_obj:
        format_obj, _ = models.Format.objects.get_or_create(format=format_name)
        cve_obj.format = format_obj
        cve_obj.save()

def save_reference_data(name:str, url:str, cve_obj:models.CVE)->None:
    if name and cve_obj:
        reference_data, p = models.Reference.objects.get_or_create(name=name, url=url)
        reference_data.cve.add(cve_obj)
        reference_data.save()
        return reference_data

def save_refsource(name:str, reference_obj:models.Reference)->None:
    if name:
        refsource_obj, _ = models.Refsource.objects.get_or_create(name=name)
        if reference_obj:
            refsource_obj.reference.add(reference_obj)
            refsource_obj.save()


def save_tag_to_reference(tag_name:str, reference_obj:models.Reference)->None:
    if tag_name:
        tag_name = tag_name.lower()
        tag_name = tag_name.replace(' ' ,'_')
        tag_obj, _ = models.Tag.objects.get_or_create(name=tag_name)
    if reference_obj:
        tag_obj.reference.add(reference_obj)
    tag_obj.save()

def get_and_save_cpe(is_vulnerable:bool, uri:str, cve_obj:models.CVE):
    if uri and cve_obj:
        cpe_obj, _ = models.CPEMatch.objects.get_or_create(is_vulnerable=is_vulnerable, uri=uri)
        cpe_obj.cve.add(cve_obj)
        cpe_obj.save()
        return cpe_obj

def save_base_metric_v2(base_metric_v2:dict, cve_obj:models.CVE):
    vector_str = base_metric_v2.get('cvssV2', {}).get('vectorString')
    if vector_str:
        vector_obj, _ = models.Vector.objects.get_or_create(vector = vector_str)

    cvss_v2_obj, _ = models.CVSSV2.objects.get_or_create(
        version=base_metric_v2['cvssV2']['version'],
        access_vector=base_metric_v2['cvssV2']['accessVector'],
        access_complexity=base_metric_v2['cvssV2']['accessComplexity'],
        authentication=base_metric_v2['cvssV2']['authentication'],
        confidentiality_impact=base_metric_v2['cvssV2']['confidentialityImpact'],
        integrity_impact=base_metric_v2['cvssV2']['integrityImpact'],
        availability_impact=base_metric_v2['cvssV2']['availabilityImpact'],
        base_score=base_metric_v2['cvssV2']['baseScore'],
        vector=vector_obj
    )

    base_metric_v2_obj, _ = models.BaseMetricV2.objects.get_or_create(
        cvss_v2 = cvss_v2_obj,
        severity=base_metric_v2['severity'],
        exploitability_score=base_metric_v2['exploitabilityScore'],
        impact_score=base_metric_v2['impactScore'],
        is_obtain_all_privilege=base_metric_v2['obtainAllPrivilege'],
        is_obtain_user_privilege=base_metric_v2['obtainUserPrivilege'],
        is_obtain_other_privilege=base_metric_v2['obtainOtherPrivilege'],
        # CVE-2016-0099 nie ma UserInteractionRequired
        is_user_interaction_required=base_metric_v2.get('userInteractionRequired', None),
    )
    base_metric_v2_obj.cve.add(cve_obj)
    base_metric_v2_obj.save()


def save_base_metric_v3(base_metric_v3:dict, cve_obj:models.CVE):
    vector_str = base_metric_v3.get('cvssV3', {}).get('vectorString')
    if vector_str:
        vector_obj, _ = models.Vector.objects.get_or_create(vector = vector_str)
    
    cvss_v3_obj, _ = models.CVSSV3.objects.get_or_create(
        version=base_metric_v3['cvssV3']['version'],
        vector=vector_obj,
        attack_vector=base_metric_v3['cvssV3']['attackVector'],
        attack_complexity=base_metric_v3['cvssV3']['attackComplexity'],
        privileges_required=base_metric_v3['cvssV3']['privilegesRequired'],
        user_interaction=base_metric_v3['cvssV3']['privilegesRequired'],
        scope=base_metric_v3['cvssV3']['scope'],
        confidentiality_impact=base_metric_v3['cvssV3']['confidentialityImpact'],
        integrity_impact=base_metric_v3['cvssV3']['integrityImpact'],
        availability_impact=base_metric_v3['cvssV3']['availabilityImpact'],
        base_score=base_metric_v3['cvssV3']['baseScore'],
        base_severity=base_metric_v3['cvssV3']['baseSeverity']
    )

    base_metric_v3_obj, _ = models.BaseMetricV3.objects.get_or_create(
        cvss_v3 = cvss_v3_obj,
        exploitability_score=base_metric_v3['exploitabilityScore'],
        impact_score=base_metric_v3['impactScore'],
    )
    base_metric_v3_obj.cve.add(cve_obj)
    base_metric_v3_obj.save()


def save_data(filepath:str)->None:
    data = get_dict_from_json_file(filepath)
    cve_list = data.get('CVE_Items')
    for cve in cve_list:
        try:
            # print(cve['cve']['CVE_data_meta']['ID'])
            for problemtype_data in cve['cve']['problemtype']['problemtype_data']:
                description = problemtype_data['description']
                cwe_id =  description[0].get('value') if description else None

            cve_obj = get_and_save_cve(
                id=cve['cve']['CVE_data_meta']['ID'],
                published = cve['publishedDate'],
                modified=cve['lastModifiedDate'],
                description= cve['cve']['description']['description_data'][0]['value'],
                cwe_id=cwe_id
            )

            version = cve.get('cve', {}).get('data_version')
            save_version_to_cve(version, cve_obj)
            save_assigner_to_cve(cve.get('cve', {}).get('CVE_data_meta', {}).get('ASSIGNER'), cve_obj)
            save_format_to_cve(cve.get('cve', {}).get('data_format'), cve_obj)


            references_list= cve.get('cve', {}).get('references', {}).get('reference_data')
            for ref in references_list:
                reference_data_obj = save_reference_data(
                    name = ref['name'],
                    url = ref['url'],
                    cve_obj=cve_obj
                )
                save_refsource(ref.get('refsource'), reference_data_obj)
                for tag in ref.get('tags'):
                    tag = save_tag_to_reference(tag, reference_data_obj)

            for node in cve.get('configurations', {}).get('nodes'):
                cpe_match_list= node.get('cpe_match')
                for cpe_match in cpe_match_list:
                    get_and_save_cpe(
                        uri=cpe_match['cpe23Uri'],
                        is_vulnerable=cpe_match['vulnerable'],
                        cve_obj=cve_obj
                    )

            base_metric_v2:dict = cve.get('impact', {}).get('baseMetricV2')
            if base_metric_v2:
                save_base_metric_v2(base_metric_v2, cve_obj)

            base_metric_v3:dict = cve.get('impact', {}).get('baseMetricV3')
            if base_metric_v3:
                save_base_metric_v3(base_metric_v3, cve_obj)

        except BaseException as e:
            print(e)
            print(type(e))
            print('[Error] CVE ID: ', cve['cve']['CVE_data_meta']['ID'])

def main():
    files_url = get_files_url()
    files_url = [
        # 'https://nvd.nist.gov//feeds/json/cve/1.1/nvdcve-1.1-modified.json.zip',
        # 'https://nvd.nist.gov//feeds/json/cve/1.1/nvdcve-1.1-recent.json.zip',
        # 'https://nvd.nist.gov//feeds/json/cve/1.1/nvdcve-1.1-2022.json.zip',
        # 'https://nvd.nist.gov//feeds/json/cve/1.1/nvdcve-1.1-2021.json.zip',
        # 'https://nvd.nist.gov//feeds/json/cve/1.1/nvdcve-1.1-2020.json.zip',
        # 'https://nvd.nist.gov//feeds/json/cve/1.1/nvdcve-1.1-2019.json.zip',
        # 'https://nvd.nist.gov//feeds/json/cve/1.1/nvdcve-1.1-2018.json.zip',
        # 'https://nvd.nist.gov//feeds/json/cve/1.1/nvdcve-1.1-2017.json.zip',
        # 'https://nvd.nist.gov//feeds/json/cve/1.1/nvdcve-1.1-2016.json.zip',
        'https://nvd.nist.gov//feeds/json/cve/1.1/nvdcve-1.1-2015.json.zip',
        # 'https://nvd.nist.gov//feeds/json/cve/1.1/nvdcve-1.1-2014.json.zip',
        # 'https://nvd.nist.gov//feeds/json/cve/1.1/nvdcve-1.1-2013.json.zip',
        # 'https://nvd.nist.gov//feeds/json/cve/1.1/nvdcve-1.1-2012.json.zip',
        # 'https://nvd.nist.gov//feeds/json/cve/1.1/nvdcve-1.1-2011.json.zip',
        # 'https://nvd.nist.gov//feeds/json/cve/1.1/nvdcve-1.1-2010.json.zip',
        # 'https://nvd.nist.gov//feeds/json/cve/1.1/nvdcve-1.1-2009.json.zip',
        # 'https://nvd.nist.gov//feeds/json/cve/1.1/nvdcve-1.1-2008.json.zip',
        # 'https://nvd.nist.gov//feeds/json/cve/1.1/nvdcve-1.1-2007.json.zip',
        # 'https://nvd.nist.gov//feeds/json/cve/1.1/nvdcve-1.1-2006.json.zip',
        # 'https://nvd.nist.gov//feeds/json/cve/1.1/nvdcve-1.1-2005.json.zip',
        # 'https://nvd.nist.gov//feeds/json/cve/1.1/nvdcve-1.1-2004.json.zip',
        # 'https://nvd.nist.gov//feeds/json/cve/1.1/nvdcve-1.1-2003.json.zip',
        # 'https://nvd.nist.gov//feeds/json/cve/1.1/nvdcve-1.1-2002.json.zip'
    ]
    for f_url in files_url:
        extracted_file_name = download_file(file_url = f_url)
        print('extracted_file_name: ', extracted_file_name)
        save_data(extracted_file_name)
