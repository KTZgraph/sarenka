""" 
pip install django-extensions
settings.py dopisać INSTALLED_APPS =[ ..., 'django-extensions', ...]
stworzyć folder srcripts a w nim scripts/__init__.py pusty

załadowanie danych:
python manage.py runscript cwe_list_load # BEZ ROZSZRZERZENIA PY
"""

from requests import get
from os import remove, path
from zipfile import ZipFile
from pathlib import Path
from xml.dom import minidom

from apps.vulnerabilities.models import CWE

DIR_PATH = Path(__file__).parent.absolute()

def download():
    file_url = 'https://cwe.mitre.org/data/xml/cwec_latest.xml.zip'
    zip_filename = file_url.split('/')[-1]
    data  = get(file_url)
    with open(DIR_PATH.joinpath(zip_filename), 'wb') as f:
        f.write(data.content)
    return zip_filename

def unzip(zip_filename:str):
    zip_filename = DIR_PATH.joinpath(zip_filename)
    with ZipFile(zip_filename, 'r') as zip_ref:
        extracted_file_name = zip_ref.namelist()
        zip_ref.extractall(DIR_PATH)

    remove(zip_filename)
    return extracted_file_name[0] # tylko jeden plik w zipie

def parse(extracted_file_name:str):
    cwe_list = []
    extracted_file_name = str(DIR_PATH.joinpath(extracted_file_name))

    dom_tree = minidom.parse(extracted_file_name)
    weakness_catalog = dom_tree.documentElement # TODO
    weakness = dom_tree.getElementsByTagName('Weakness')
    for cwe in weakness:
        cwe_obj = {}
        if cwe.hasAttribute('ID'):
            cwe_obj['id'] = cwe.getAttribute('ID')
        if cwe.hasAttribute('Name'):
            cwe_obj['name'] = cwe.getAttribute('Name')
        if cwe.hasAttribute('Abstraction'):
            cwe_obj['abstraction'] = cwe.getAttribute('Abstraction')
        if cwe.hasAttribute('Structure'):
            cwe_obj['structure'] = cwe.getAttribute('Structure')
        if cwe.hasAttribute('Status'):
            cwe_obj['status'] = cwe.getAttribute('Status')

        cwe_obj['description'] = cwe.getElementsByTagName('Description')[0].childNodes[0].data

        try:
            cwe_obj['extended_description'] = cwe.getElementsByTagName('Extended_Description')[0].childNodes[0].data
            if '\n            ' in cwe_obj['extended_description']:
                cwe_obj['extended_description'] = ''
        except (IndexError, AttributeError):
            cwe_obj['extended_description'] = ''

        cwe_list.append(cwe_obj)

    remove(extracted_file_name)
    return cwe_list

def run():
    zip_filename = download()
    extracted_file_name = unzip(zip_filename)
    cwe_list = parse(extracted_file_name)

    CWE.objects.all().delete()

    for cwe in cwe_list:
        obj, created = CWE.objects.get_or_create(
            id = cwe["id"],
            name=cwe["name"],
            abstraction=cwe["abstraction"],
            structure = cwe["structure"],
            status = cwe["status"],
            description = cwe["description"],
            extended_description = cwe["extended_description"]
        )

