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

def run()->list:
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

    json_filenames.sort() #modified and recent on the end
    for f in json_filenames:
        print(f)

if __name__ =="__main__":
    run()