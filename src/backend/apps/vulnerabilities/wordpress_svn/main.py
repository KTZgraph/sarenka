"""
driver download page: https://chromedriver.storage.googleapis.com/index.html?path=102.0.5005.61/
wordpress plugins repo : https://plugins.svn.wordpress.org/
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import requests
import re
import json
from typing import Dict, Optional, List, TypedDict, Mapping


MAIN_URL = "https://plugins.svn.wordpress.org/"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"
}


# selenium settings
options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")


DRIVER_PATH = "chromedriver.exe"
s = Service(DRIVER_PATH)
driver = webdriver.Chrome(service=s, options=options)


#################################################


def get_page_content(URL: str) -> str:
    driver.get(URL)
    return driver.page_source


def get_page_links(page_source: str, base_url: str) -> Dict[str, str]:
    soup = BeautifulSoup(page_source, "html.parser")
    links = soup.select("a")

    links_dict = {}
    for link in links:
        key = link.get_text()
        key = key.replace("/", "")
        value = link.get("href")
        value = f"{base_url}{value}"
        links_dict[key] = value

    return links_dict


def save_dict_as_json(data: dict, filename: str) -> None:
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

#helper
def get_plugin_version_readme_file(plugin_version_url: str) -> tuple[Optional[str], Optional[str]]:
    """https://plugins.svn.wordpress.org/0-errors/tags/0.2/readme.txt

    === 0-Errors ===
    ...
    Stable tag: 0.2

    Args:
        plugin_version_url (str): _description_

    Returns:
        str: _description_
    """
    readme_url = f"{plugin_version_url}readme.txt"

    headers = {k:v for k,v in HEADERS.items()}
    headers.update({'Range':'bytes=0-2000000'})

    readme_file = requests.get(readme_url, headers=headers, stream=True)
    
    if readme_file.status_code == 200:
        return readme_file
    
    return None

def get_plugin_version_readme_info(plugin_version_url:str)->tuple[Optional[str], Optional[str]]:
    # u góry pliku znajdowanie tytułu
    # === 0-Errors ===
    # === Late Caching for Feeds ===
    #https://plugins.svn.wordpress.org/0-delay-late-caching-for-feeds/tags/1.0.1/readme.md
    # Late Caching for Feeds
    # ===
    # Stable tag: 0.2
    # Stable tag:         1.0.2
    title_readme = None
    stable_readme = None

    readme_file: requests.models.Response = get_plugin_version_readme_file(plugin_version_url)
    if not readme_file:
        return title_readme, stable_readme

    title_pattern = r'=== (\w+[-,\s]*)+==='
    stable_pattern = r'Stable tag:\s+(\d\.*)+'

    chunk: bytes
    for chunk in readme_file.iter_content(chunk_size=1024):
        txt = str(chunk)
        if re.search(title_pattern, txt):
            title_readme = re.search(title_pattern, txt).group(0)
        
        if re.search(stable_pattern, txt):
            stable_readme = re.search(stable_pattern, txt).group(0)

        if title_readme and stable_readme:
            break

    return title_readme, stable_readme


class PluginDetails(TypedDict):
    plugin_url: Dict[str, str]  # tutaj zawsze są
    versions: Optional[Dict[str, str]]  # śłownik albo None
    versions_short: Optional[List[str]]  # lista albo None

def get_plugin_versions_info(plugin_versions_links:Dict[str, str])->Dict[str, str]:
    versions_info = {}
    for version_name, version_url in plugin_versions_links.items():
        title_readme, stable_readme = get_plugin_version_readme_info(version_url)
        versions_info[version_name] = {
            'version_url': version_url,
            'title_readme': title_readme,
            'stable_readme': stable_readme
        }
    return versions_info

def get_plugins_versions_links(
    main_links: Dict[str, str]
) -> Mapping[str, PluginDetails]:
    plugins_versions_links = {}

    # ograniczam tymczasowo liczbę #TODO
    for plugin_name in list(main_links.keys())[:5]:  
        plugin_main_url = main_links[plugin_name]
        plugin_versions_info_url = f"{plugin_main_url}tags/"
        plugin_versions_page_content = get_page_content(plugin_versions_info_url)
        plugin_versions_links = get_page_links(
            plugin_versions_page_content, plugin_versions_info_url
        )

        plugin_versions_links.pop("..", None)
        plugin_versions_links.pop("Apache Subversion", None)

        versions_info = get_plugin_versions_info(plugin_versions_links)
        plugins_versions_links[plugin_name] = {
            "plugin_url": plugin_main_url,
            "versions": versions_info if versions_info else None,
            "versions_short": list(plugin_versions_links.keys()) if plugin_versions_links else None,
        }

    return plugins_versions_links


def main():
    page_content: str = get_page_content(MAIN_URL)
    main_links: dict = get_page_links(page_content, MAIN_URL)
    main_links.pop("Apache Subversion", None)
    save_dict_as_json(main_links, "plugins_main.json")

    plugins_versions_links = get_plugins_versions_links(main_links)
    save_dict_as_json(plugins_versions_links, "plugins_versions.json")


if __name__ == "__main__":
    main()
    driver.quit()  # tylko na końcu
