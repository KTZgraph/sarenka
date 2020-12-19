import json
import requests
import os
from functools import lru_cache
from rest_framework.reverse import reverse


class CVEAll:
    feeder_url = "https://raw.githubusercontent.com/pawlaczyk/sarenka_tools/master/cve_all.json"
    file_name = "cve_all.json"
    source_nist = "https://nvd.nist.gov/vuln/full-listing"
    nist_url = "https://nvd.nist.gov/vuln/detail/"

    def __init__(self):
        self.__data = self.get_data()

    @property
    @lru_cache
    def values(self):
        return self.__data


    @staticmethod
    def feed():
        """Gdy nie ma pliku zapisuje go lokalnie"""
        result = requests.get(CVEAll.feeder_url).json()
        with open(CVEAll.file_name, 'w') as fp:
            json.dump(result, fp,  indent=4)

    @staticmethod
    def get_data():
        if not os.path.isfile(CVEAll.file_name):
            # jak nie ma pliku lokalnie to go zapisuje
            CVEAll.feed()

        with open(CVEAll.file_name) as json_file:
            data = json.load(json_file)

        return data # zwraca w postaci jsona

    def render_output(self, host_address):
        """Dodaje url do sarenki i zewnętrzen do mitre wskazujące na mitre"""
        result = {}
        result.update({"created_at": self.values["created_at"]})
        result.update({"source": self.source_nist})

        all_cves = self.values["cve_all"] #lista słowników
        for cve in all_cves:
            cve_id = cve["cve_code"]
            cve["nist_url"] = f"{self.nist_url}{cve_id}"
            cve["sarenka_url"] = host_address + reverse('get_by_cve', kwargs={"code": cve_id})

        result.update({"cve_all": all_cves})

        return result