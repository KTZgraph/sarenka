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
        # print(href)
        if href.split(".")[-1] == "zip":
            files_urls.append(f'{base_url}{href}')

    return files_urls
    # https://nvd.nist.gov/feeds/json/cve/1.1/nvdcve-1.1-modified.json.zip
    # https://nvd.nist.gov/feeds/json/cve/1.1/nvdcve-1.1-2022.json.zip

def download_file(file_url:str)->str:
    zip_filename = file_url.split("/")[-1]
    data = requests.get(file_url)
    #save zip file
    with open(zip_filename, "wb") as f:
        f.write(data.content)
    # unzip downloaded file
    with ZipFile(zip_filename, "r") as zip_ref:
        extracted_file_name = zip_ref.namelist()
        zip_ref.extractall('.')

    os.remove(zip_filename)
    #only one file i zip package
    return extracted_file_name[0]

# ------------------- database


def get_and_save_version(version:str, cve_obj:models.CVE)->None:
    print("cve_obj: ", cve_obj)
    print("type cve_obj: ", type(cve_obj))
    if version:
        data_version, _ = models.Version.objects.get_or_create(version=float(version))
        print('data_version: ', data_version)
        print("cve_obj: ", cve_obj)
        print("type cve_obj: ", type(cve_obj))
        if cve_obj is not None and data_version:
            cve_obj.version.add(data_version)
            cve_obj.save()

def get_and_save_assigner(assigner_email:str, cve_obj:models.CVE)->None:
    assigner_obj, _ = models.Assigner.objects.get_or_create(email=assigner_email)
    if cve_obj:
        assigner_obj.cve.add(cve_obj)
        assigner_obj.save()

def get_and_save_data_format(name:str, cve_obj=None):
    data_format = models.DataFormat.objects.get_or_create(name=name)
    data_format.cve.add(cve_obj)
    data_format.save()
    return data_format

def get_and_save_reference_data(name:str, url:str, cve_obj=None):
    reference_data = models.ReferenceData.objects.get_or_create(name=name, url=url)
    reference_data.cve.add(cve_obj)
    reference_data.save()
    return reference_data

def get_and_save_refsource_reference(name:str, reference_data_obj=None):
    refsource_reference_obj = models.RefsourceReference.objects.get_or_create(name=name)
    refsource_reference_obj.reference_data.add(reference_data_obj)
    refsource_reference_obj.save()
    return refsource_reference_obj

def get_and_save_tag(name:str, reference_data_obj): #zwraca tag obiekt  zbazy
    name = name.lower()
    name = name.replace(' ' ,'_')
    tag_obj = models.TagReference.objects.get_or_create(name=name)
    return tag_obj

def get_and_save_cpe(is_vulnerable:bool, uri:str, cve_obj=None):
    # print(f'\n\n\nis_vulnerable: {is_vulnerable}\n uri: {uri}')
    cpe_obj = models.CPEMatch(is_vulnerable=is_vulnerable, uri=uri)
    cpe_obj.cve.add(cve_obj)
    cpe_obj.save()
    return cpe_obj

def get_and_save_base_metric_v2(base_metric_v2:dict, cve_obj=None):
    vector_obj = models.Vector.objects.get_or_create(base_metric_v2['cvssV2']['vectorString'])

    cvss_v2_obj = models.CVSSV2.objects.get_or_create(
        vector=vector_obj,
        version=base_metric_v2['cvssV2']['version'],
        access_vector=base_metric_v2['cvssV2']['accessVector'],
        access_complexity=base_metric_v2['cvssV2']['accessComplexity'],
        authentication=base_metric_v2['cvssV2']['authentication'],
        confidentiality_impact=base_metric_v2['cvssV2']['confidentialityImpact'],
        integrity_impact=base_metric_v2['cvssV2']['integrityImpact'],
        availability_impact=base_metric_v2['cvssV2']['availabilityImpact'],
        base_score=base_metric_v2['cvssV2']['baseScore'],
    )

    base_metric_v2_obj = models.BaseMetricV2.objects.get_or_create(
        cve=cve_obj,
        cvss_v2=cvss_v2_obj,
        severity=base_metric_v2['severity'],
        exploitability_score=base_metric_v2['exploitabilityScore'],
        impact_score=base_metric_v2['impactScore'],
        is_obtain_all_privilege=base_metric_v2['obtainAllPrivilege'],
        is_obtain_user_privilege=base_metric_v2['obtainUserPrivilege'],
        is_obtain_other_privilege=base_metric_v2['obtainOtherPrivilege'],
        is_user_interaction_required=base_metric_v2['userInteractionRequired'],
    )

    return base_metric_v2_obj


def get_and_save_base_metric_v3(base_metric_v3:dict, cve_obj=None):
    vector_obj = models.Vector.objects.get_or_create(base_metric_v3['cvssV3']['vectorString'])
    
    cvss_v3_obj = models.CVSS3.objects.get_or_create(
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
        base_severity=base_metric_v3['cvssV3']['baseSeverity'],
    )

    base_metric_v3_obj = models.BaseMetricV3.objects.get_or_create(
        cve=cve_obj,
        vector=vector_obj,
        cvss_v3 = cvss_v3_obj,
        exploitability_score=base_metric_v3['exploitabilityScore'],
        impact_score=base_metric_v3['impactScore'],
    )

    return base_metric_v3_obj


def save_data(filepath:str)->None:
    data = get_dict_from_json_file(filepath)
    cve_list = data.get('CVE_Items')
    for cve in cve_list[10:20]:
        for problemtype_data in cve['cve']['problemtype']['problemtype_data']:
            description = problemtype_data['description']
            cwe_id =  description[0].get('value') if description else None

        cve_id = cve['cve']['CVE_data_meta']['ID']
        cve_obj = get_and_save_cve(
            id=cve['cve']['CVE_data_meta']['ID'],
            published = cve['publishedDate'],
            modified=cve['lastModifiedDate'],
            description= cve['cve']['description']['description_data'][0]['value'],
            cwe_id=cwe_id
        )
        version = cve.get('cve').get('data_version')
        get_and_save_version(version, cve_obj)


        # get_and_save_assigner(cve['cve']['CVE_data_meta']['ASSIGNER'], cve_obj)
        
        
        # data_format_obj = get_and_save_data_format(cve['cve']['data_format'], cve_obj)

        # # print('#####################################################')
        # references_dict= cve['cve']['references']['reference_data']
        # for ref in references_dict:

        #     reference_data__obj = get_and_save_reference_data(
        #         name = ref['name'],
        #         url = ref['url'],
        #         cve_obj=cve_obj
        #     )

        #     refsource_reference = get_and_save_refsource_reference(name=ref['refsource'], reference_data_obj = reference_data__obj)

        #     for tag in ref['tags']:
        #         tag = get_and_save_tag(name=tag, reference_data_obj =reference_data__obj)

        # for node in cve.get('configurations', {}).get('nodes'):
        #     cpe_match_list= node.get('cpe_match')
        #     for cpe_match in cpe_match_list:
        #         get_and_save_cpe(
        #             uri=cpe_match['cpe23Uri'],
        #             is_vulnerable=cpe_match['cpe23Uri'],
        #             cve_obj=None
        #         )

        # base_metric_v2:dict = cve.get('impact', {}).get('baseMetricV2')
        # if base_metric_v2:
        #     get_and_save_base_metric_v2(base_metric_v2, cve_obj=cve_obj)

        # base_metric_v3:dict = cve.get('impact', {}).get('baseMetricV3')
        # if base_metric_v3:
        #     get_and_save_base_metric_v3(base_metric_v3, cve_obj=cve_obj)

def main():
    files_url = get_files_url()
    extracted_file_name = download_file(file_url =  files_url[-1])
    print(extracted_file_name)
    save_data(extracted_file_name)


if __name__ == '__main__':
    main()
