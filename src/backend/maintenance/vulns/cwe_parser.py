from os import remove
import json


from xml.dom import minidom
from cwe_downloader import CWEDownloader


class CWEParser:
    _data_file = "cwe_list.json"


    def __init__(self):
        self._filepath = CWEDownloader().filepath
        self._cwe_list = self.parse()

    @property
    def cwe_list(self):
        return self._cwe_list

    def parse(self, save=True):
        cwe_list = []

        dom_tree = minidom.parse(self._filepath)
        weakness_catalog = dom_tree.documentElement
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


        if save == True:
            data = {"cwe_list": cwe_list}
            with open("cwe_list.json", 'w') as f:
                json.dump(data, f)


        return cwe_list

if __name__ == "__main__":
    CWEParser().parse()