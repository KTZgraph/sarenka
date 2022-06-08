"""
driver download page: https://chromedriver.storage.googleapis.com/index.html?path=102.0.5005.61/
wordpress plugins repo : https://plugins.svn.wordpress.org/
"""
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from bs4 import BeautifulSoup
from typing import Dict, Optional, List, TypedDict, Mapping

class PluginDetails(TypedDict):
    plugin_url: Dict[str, str] #tutaj zawsze są
    versions: Optional[Dict[str, str]] #śłownik albo None
    versions_short: Optional[List[str]] # lista albo None


MAIN_URL = 'https://plugins.svn.wordpress.org/'


# selenium settings
options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")


DRIVER_PATH = 'chromedriver.exe'
s = Service(DRIVER_PATH)
driver = webdriver.Chrome(service=s, options=options)

#################################################

def get_page_content(URL:str)->str:
    driver.get(URL)
    return driver.page_source

def get_page_links(page_source:str, base_url:str)->Dict[str, str]:
    soup = BeautifulSoup(page_source, 'html.parser')
    links = soup.select('a')

    links_dict = {}
    for link in links:
        key = link.get_text()
        if 'Apache Subversion' in key:
            continue
        key = key.replace('/', '')
        value = link.get('href')
        value = f'{base_url}{value}'
        links_dict[key] = value
    
    return links_dict

def save_dict_as_json(data:dict, filename:str)->None:
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def get_plugins_versions_links(main_links:Dict[str, str])->Mapping[str, PluginDetails]:
    plugins_versions_links = {}

    for plugin_name in list(main_links.keys())[:10]: #ograniczam tymczasowo liczbę #TODO
        plugin_main_url = main_links[plugin_name]
        plugin_versions_info_url = f'{plugin_main_url}tags/'
        plugin_versions_page_content = get_page_content(plugin_versions_info_url)
        plugin_versions_links = get_page_links(plugin_versions_page_content, plugin_versions_info_url)

        plugins_versions_links[plugin_name] = {
            'plugin_url': plugin_main_url,
            'versions': plugin_versions_links if plugin_versions_links else None,
            'versions_short': list(plugin_versions_links.keys()) if plugin_versions_links else None
        }
    return plugins_versions_links



def main():
    page_content:str = get_page_content(MAIN_URL)
    main_links:dict = get_page_links(page_content, MAIN_URL)
    save_dict_as_json(main_links, 'plugins_main.json')
    plugins_versions_links = get_plugins_versions_links(main_links)
    save_dict_as_json(plugins_versions_links, 'plugins_versions.json')


if __name__ == "__main__":
    main()
    driver.quit() #tylko na końcu 