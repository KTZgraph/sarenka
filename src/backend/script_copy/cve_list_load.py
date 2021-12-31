""" 
pip install django-extensions
settings.py dopisać INSTALLED_APPS =[ ..., 'django-extensions', ...]
stworzyć folder srcripts a w nim scripts/__init__.py pusty

załadowanie danych:
python manage.py runscript cve_list_load # BEZ ROZSZRZERZENIA PY
"""
from bs4 import BeautifulSoup
from requests import get
from pathlib import Path
from zipfile import ZipFile
from os import remove
import json

from apps.vulnerabilities.models import CVE


DIR_PATH = Path(__file__).parent.absolute()
MAIN_URL = "https://nvd.nist.gov" # bez / na końcu

feeder_page = "https://nvd.nist.gov/vuln/data-feeds#JSON_FEED"


def scrap()->list:
    files_urls = []
    source  = get(feeder_page).text
    soup = BeautifulSoup(source, 'lxml')

    # <div id="divJSONFeeds" class="row">
    soup = soup.find("div", {"id": "divJSONFeeds"})
    # <table class="xml-feed-table table table-striped table-condensed">
    soup = soup.find("table") #tylko jedna tabela w sordku diva 

    for a in soup.find_all("a", href=True):
        href = a["href"]
        if href.split('.')[-1] == "zip":
            files_urls.append(MAIN_URL + href)
    
    return files_urls


def download(files_urls:list)->list:
    zip_filenames = []
    
    for file_url in files_urls:
        zip_filename = file_url.split('/')[-1]
        data  = get(file_url)
        with open(DIR_PATH.joinpath(zip_filename), 'wb') as f:
            f.write(data.content)
            zip_filenames.append(zip_filename)
    
    return zip_filenames

def unzip(zip_filenames:list)->list:
    json_filenames = []

    for zip_filename in zip_filenames:
        zip_filename = DIR_PATH.joinpath(zip_filename)

        with ZipFile(zip_filename, 'r') as zip_ref:
            extracted_file_name = zip_ref.namelist()
            zip_ref.extractall(DIR_PATH)

        remove(zip_filename)
        json_filenames.append(extracted_file_name[0]) #tylko jeden plik w zipie

    return json_filenames


class CVEParser:
    #TODO z czystego kodu zwortki saprawdzić
    @staticmethod
    def parse(cve_dict:dict)->dict:

        response = {
            "id": CVEParser.parse_id(cve_dict),
            "cwe": CVEParser.parse_cwe(cve_dict),
            "references": CVEParser.parse_references(cve_dict),
            "description" : CVEParser.parse_description(cve_dict),
            "cpe": CVEParser.parse_cpe(cve_dict),
            "cvss_v3": CVEParser.parse_cvssV3(cve_dict),
            "cvss_v2": CVEParser.parse_cvssV2(cve_dict),
            "last_modified_date": CVEParser.parse_lastModifiedDate(cve_dict),
            "published_date":CVEParser.parse_publishedDate(cve_dict),
        }

        return response

    @staticmethod
    def parse_id(cve_dict:dict)->str:
        return cve_dict["CVE_data_meta"]["ID"]

    @staticmethod
    def parse_cwe(cve_dict:dict)->str:
        """
        "problemtype" : {
             "problemtype_data" : [ {
               "description" : [ {
                 "lang" : "en",
                 "value" : "CWE-203"
               } ]
             } ]
           }
        """
        cwe = cve_dict.get("problemtype").get("problemtype_data", None)
        cwe = cwe[0].get("description", None) if cwe else None
        cwe = cwe[0]["value"] if cwe else None
        return cwe

    @staticmethod
    def parse_references(cve_dict:dict)->list[list]:
        """
        "references" : {
            "reference_data" : [ {
              "url" : "https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00515.html",
              "name" : "https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00515.html",
              "refsource" : "MISC",
              "tags" : [ "Vendor Advisory" ]
            }, {
              "url" : "https://security.netapp.com/advisory/ntap-20210827-0008/",
              "name" : "https://security.netapp.com/advisory/ntap-20210827-0008/",
              "refsource" : "CONFIRM",
              "tags" : [ "Third Party Advisory" ]
            } ]
          },
        """
        reference_data =  cve_dict["references"]["reference_data"] #list
        
        reference_urls = []
        for ref in reference_data:
            reference_urls.append([
                ref.get("url", None), #str url
                ref.get("refsource", None), #str MISC / CONFIRM
                ref.get("tags", None) # str
            ])

        return reference_urls
   
    @staticmethod
    def parse_description(cve_dict:dict)->str:
        """
        "description" : {
          "description_data" : [ {
            "lang" : "en",
            "value" : "Observable timing discrepancy in Intel(R) IPP before version 2020 update 1 may allow authorized user to potentially enable information disclosure via local access."
          } ]
        }
        """
        description = cve_dict.get("description", None)
        description = description.get("description_data", None) if description else None
        description = description[0]["value"] if description else None

        return description

    @staticmethod
    def parse_cpe(cve_dict:dict)->list: 
        """
        "configurations" : {
        "CVE_data_version" : "4.0",
        "nodes" : [ {
            "operator" : "OR",
            "children" : [ ],
            "cpe_match" : [ {
            "vulnerable" : true,
            "cpe23Uri" : "cpe:2.3:a:intel:integrated_performance_primitives_cryptography:2019:-:*:*:*:*:*:*",
            "cpe_name" : [ ]
            }, {
            "vulnerable" : true,
            "cpe23Uri" : "cpe:2.3:a:intel:integrated_performance_primitives_cryptography:2019:update_1:*:*:*:*:*:*",
            "cpe_name" : [ ]
            }, {
            "vulnerable" : true,
            "cpe23Uri" : "cpe:2.3:a:intel:integrated_performance_primitives_cryptography:2019:update_2:*:*:*:*:*:*",
            "cpe_name" : [ ]
            }, {
            "vulnerable" : true,
            "cpe23Uri" : "cpe:2.3:a:intel:integrated_performance_primitives_cryptography:2019:update_3:*:*:*:*:*:*",
            "cpe_name" : [ ]
            }, {
            "vulnerable" : true,
            "cpe23Uri" : "cpe:2.3:a:intel:integrated_performance_primitives_cryptography:2019:update_4:*:*:*:*:*:*",
            "cpe_name" : [ ]
            }, {
            "vulnerable" : true,
            "cpe23Uri" : "cpe:2.3:a:intel:integrated_performance_primitives_cryptography:2020:-:*:*:*:*:*:*",
            "cpe_name" : [ ]
            }, {
            "vulnerable" : true,
            "cpe23Uri" : "cpe:2.3:a:intel:sgx_dcap:*:*:*:*:*:linux:*:*",
            "versionEndIncluding" : "1.10.100.4",
            "cpe_name" : [ ]
            }, {
            "vulnerable" : true,
            "cpe23Uri" : "cpe:2.3:a:intel:sgx_dcap:*:*:*:*:*:windows:*:*",
            "versionEndIncluding" : "1.10.100.4",
            "cpe_name" : [ ]
            }, {
            "vulnerable" : true,
            "cpe23Uri" : "cpe:2.3:a:intel:sgx_psw:*:*:*:*:*:windows:*:*",
            "versionEndIncluding" : "2.12.100.4",
            "cpe_name" : [ ]
            }, {
            "vulnerable" : true,
            "cpe23Uri" : "cpe:2.3:a:intel:sgx_psw:*:*:*:*:*:linux:*:*",
            "versionEndIncluding" : "2.13.100.4",
            "cpe_name" : [ ]
            }, {
            "vulnerable" : true,
            "cpe23Uri" : "cpe:2.3:a:intel:sgx_sdk:*:*:*:*:*:windows:*:*",
            "versionEndIncluding" : "2.12.100.4",
            "cpe_name" : [ ]
            }, {
            "vulnerable" : true,
            "cpe23Uri" : "cpe:2.3:a:intel:sgx_sdk:*:*:*:*:*:linux:*:*",
            "versionEndIncluding" : "2.13.100.4",
            "cpe_name" : [ ]
            } ]
        } ]
        },
        """
        cpe_match_list = cve_dict.get("configurations", None)
        cpe_match_list = cpe_match_list.get("nodes", None) if cpe_match_list else None
        cpe_match_list = cpe_match_list[0].get("cpe_match", None) if cpe_match_list else None
        cpe = []
        
        if cpe_match_list:
            for cpe_match in cpe_match_list:
                cpe.append([
                    cpe_match.get("vulnerable", None), #bool
                    cpe_match.get("cpe23Uri", None), #TODO rożne wersje uri moga być
                    cpe_match.get("versionEndIncluding", None), #str
                    cpe_match.get("versionEndExcluding", None), #str "CVE-2021-0053"
                ])

        return cpe

    @staticmethod #TODO
    def parse_cvssV3(cve_dict:dict)->list: #TODO: przypomnieć sobie skąłdowe werktora
        impact = cve_dict.get("impact",None)
        baseMetricV3 = impact.get("baseMetricV3", None) if impact else None
        cvssV3 = baseMetricV3.get("cvssV3", None) if baseMetricV3 else None

        if cvssV3:
            return [
                cvssV3.get("version", None),
                cvssV3.get("vectorString", None),
                cvssV3.get("baseScore", None),
                cvssV3.get("baseSeverity", None),

                baseMetricV3.get("exploitabilityScore", None),
                baseMetricV3.get("impactScore", None)
            ]
        return []

    @staticmethod   #TODO
    def parse_cvssV2(cve_dict:dict)->list: #TODO: przypomnieć sobie skąłdowe werktora
        impact = cve_dict.get("impact",None)
        baseMetricV2 = impact.get("baseMetricV2", None) if impact else None
        cvssV2 = baseMetricV2.get("cvssV2", None) if baseMetricV2 else None

        if cvssV2:
            return [
                cvssV2.get("version", None),
                cvssV2.get("vectorString", None),
                cvssV2.get("baseScore", None),
                cvssV2.get("version", None),
                cvssV2.get("baseSeverity", None),

                baseMetricV2.get("severity", None),
                baseMetricV2.get("exploitabilityScore", None),
                baseMetricV2.get("impactScore", None),

                #te nizej moze z wektoor stringa?
                baseMetricV2.get("acInsufInfo", None),
                baseMetricV2.get("obtainAllPrivilege", None),
                baseMetricV2.get("obtainUserPrivilege", None),
                baseMetricV2.get("obtainOtherPrivilege", None),
                baseMetricV2.get("userInteractionRequired", None),
            ]

        return []

    @staticmethod
    def parse_lastModifiedDate(cve_dict:dict)->str:
        return cve_dict.get("lastModifiedDate", None)
    
    @staticmethod
    def parse_publishedDate(cve_dict:dict)->str:
        return cve_dict.get("publishedDate", None)



def parse(json_filenames:list)->list:
    json_filenames.sort() #modified and recent on the end
    # for f in json_filenames:
    #     print(f)

    first_file = json_filenames[0]
    first_file = str(DIR_PATH.joinpath(first_file))
    with open(first_file) as json_file: 
        data = json.load(json_file)

    parsed_list = []
    for cve_data in data['CVE_Items']:
        parsed_list.append(CVEParser.parse(cve_data["cve"]))

    return parsed_list
    
def run():
    
    # files_urls = scrap()
    # zip_filenames = download(files_urls)
    # json_filenames = unzip(zip_filenames)
    json_filenames = [
    'nvdcve-1.1-modified.json', 
    'nvdcve-1.1-recent.json', 
    'nvdcve-1.1-2021.json', 
    'nvdcve-1.1-2020.json', 
    'nvdcve-1.1-2019.json', 
    'nvdcve-1.1-2018.json', 
    'nvdcve-1.1-2017.json', 
    'nvdcve-1.1-2016.json', 
    'nvdcve-1.1-2015.json', 
    'nvdcve-1.1-2014.json', 
    'nvdcve-1.1-2013.json', 
    'nvdcve-1.1-2012.json', 
    'nvdcve-1.1-2011.json', 
    'nvdcve-1.1-2010.json', 
    'nvdcve-1.1-2009.json', 
    'nvdcve-1.1-2008.json', 
    'nvdcve-1.1-2007.json', 
    'nvdcve-1.1-2006.json', 
    'nvdcve-1.1-2005.json', 
    'nvdcve-1.1-2004.json', 
    'nvdcve-1.1-2003.json', 
    'nvdcve-1.1-2002.json'
    ]

    CVE.objects.all().delete()
    cve_parsed_list = parse(json_filenames)
    for i in cve_parsed_list:
        print(i)

