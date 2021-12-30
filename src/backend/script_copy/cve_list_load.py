""" 
pip install django-extensions
settings.py dopisać INSTALLED_APPS =[ ..., 'django-extensions', ...]
stworzyć folder srcripts a w nim scripts/__init__.py pusty

załadowanie danych:
python manage.py runscript cve_list_load # BEZ ROZSZRZERZENIA PY
"""
from bs4 import BeautifulSoup
import requests

MAIN_URL = "https://nvd.nist.gov" # bez / na końcu

feeder_page = "https://nvd.nist.gov/vuln/data-feeds#JSON_FEED"


def scrap()->list:
    files_urls = []
    source  = requests.get(feeder_page).text
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


def download(files_urls:list):
    pass

if __name__ =="__main__":
    scrap()