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
        CWE.objects.get_or_create(
            id= w['@ID'], #musi być
            name = 'test', #w['@Name'],  #musi być
            abstraction = 'test', #w['@Abstraction'],
            structure = 'test', # w['@Structure'],
            status = 'test', #w['@Status'],
            description = 'test', # w['Description'], #bez małpy
            extended_description = 'test' #w['Extended_Description']["xhtml:p"][0]
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