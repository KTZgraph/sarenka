import json
import requests
import os
from functools import lru_cache
from rest_framework.reverse import reverse


class CWEAll:
    feeder_url = "https://raw.githubusercontent.com/pawlaczyk/sarenka_tools/master/cwe_all.json"
    file_name ="cwe_all.json"
    source_cwe = "https://cwe.mitre.org/data/published/cwe_latest.pdf"
    mitre_cwe_url = "https://cwe.mitre.org/data/definitions/" # np.: https://cwe.mitre.org/data/definitions/79.html

    def __init__(self):
        self.__data = self.get_data()

    @property
    @lru_cache
    def values(self):
        return self.__data

    @staticmethod
    def feed():
        """Gdy nie ma pliku zapisuje go lokalnie"""
        result = requests.get(CWEAll.feeder_url).json()
        with open(CWEAll.file_name, 'w') as fp:
            json.dump(result, fp,  indent=4)

    @staticmethod
    def get_data():
        if not os.path.isfile(CWEAll.file_name):
            # jak nie ma pliku lokalnie to go zapisuje
            CWEAll.feed()

        with open(CWEAll.file_name) as json_file:
            data = json.load(json_file)

        return data # zwraca w postaci jsona

    def render_output(self, host_address):
        """Dodaje url do sarenki i zewnętrzen do mitre wskazujące na mitre"""
        result = {}
        result.update({"created_at": self.values["created_at"]})
        result.update({"timestamp": self.values["timestamp"]})
        result.update({"source": self.source_cwe})

        all_cwes = self.values["cwe_all"] #lista słowników
        for cwe in all_cwes:
            cwe_number = cwe["cwe_id"].split("-")[-1]
            cwe["mitre_url"] = f"{self.mitre_cwe_url}{cwe_number}.html"
            cwe["sarenka_url"] = host_address + reverse('get_by_cwe', kwargs={"id_cwe": cwe["cwe_id"]})

        result.update({"cwe_all": all_cwes})

        return result
