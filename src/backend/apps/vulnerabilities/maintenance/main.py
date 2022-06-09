import os
from typing import OrderedDict
import requests
from zipfile import ZipFile
import xmltodict, json
from ..models import CWE

CWE_FILE_URL = 'https://cwe.mitre.org/data/xml/cwec_latest.xml.zip'

def save_dict_as_json(data: dict, filename: str) -> None:
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

def get_cwe_filename(URL=CWE_FILE_URL)->str:
    zip_filename = 'cwe_list.zip'
    data = requests.get(URL)
    with open(zip_filename, "wb") as f:
        f.write(data.content)
    
    with ZipFile(zip_filename, "r") as zip_ref:
        extracted_file_name = zip_ref.namelist()
        zip_ref.extractall('./')

    os.remove(zip_filename)
    return extracted_file_name[0]  # tylko jeden plik w zipie

def get_dict_from_xml_file(xml_filepath:str)->dict: 
    #open the file
    fileptr = open(xml_filepath,"r", encoding='utf-8')
    
    #read xml content from the file
    xml_content= fileptr.read()
    # print("XML content is:")
    # print(xml_content)
    
    #change xml format to ordered dict
    my_ordered_dict: OrderedDict=xmltodict.parse(xml_content)
    # print("Ordered Dictionary is:")
    # print(my_ordered_dict)


    return dict(my_ordered_dict)

#zapisywanie do bazy danych
def save_db_cwe_data(cwe_dict:dict)->list:
    weakness:list = cwe_dict.get('Weakness_Catalog').get('Weaknesses').get('Weakness')

    for w in weakness:
        try: # mismash json
            extended_description = w['Extended_Description'].get("xhtml:p", [''])[0]
            # print(extended_description)
        except AttributeError as e:
            extended_description = w['Extended_Description']
        except KeyError as e:
            extended_description = None #some CWEs don't have Extended_Description at all

        CWE.objects.get_or_create(
            id= w['@ID'],
            name = w['@Name'],
            abstraction = w['@Abstraction'],
            structure = w['@Structure'],
            status = w['@Status'],
            description = w['Description'],
            extended_description = extended_description
        )

def main():
    # 1. pobranie listy CWE z 
    cwe_filename:str = get_cwe_filename()
    print(cwe_filename)
    cwe_dict = get_dict_from_xml_file(cwe_filename)
    save_dict_as_json(cwe_dict, 'cwe.json')
    save_db_cwe_data(cwe_dict=cwe_dict)


if __name__ == '__main__':
    main()