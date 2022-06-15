from typing import List
import requests
from bs4 import BeautifulSoup
from zipfile import ZipFile
import os
import json


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

def insert_data(filepath:str)->None:
    data = get_dict_from_json_file(filepath)
    cve_list = data.get('CVE_Items')
    for cve in cve_list[:10]:
        cve_tmp = {}
        cve_tmp['id'] = cve['cve']['CVE_data_meta']['ID']
        cve_tmp['published'] = cve['publishedDate']
        cve_tmp['modified'] = cve['lastModifiedDate']
        try:
            cve_tmp['cwe'] = cve['cve']['problemtype']['problemtype_data'][0]['description'][0]['value']
            # print(cve, '\n\n')
            print(cve_tmp)
            # break
        except IndexError:
            cve_tmp['cwe'] = -1

        # print(type(e))
        print(cve_tmp)





def main():
    files_url = get_files_url()
    extracted_file_name = download_file(file_url =  files_url[-1])
    print(extracted_file_name)
    insert_data(extracted_file_name)


if __name__ == '__main__':
    main()
