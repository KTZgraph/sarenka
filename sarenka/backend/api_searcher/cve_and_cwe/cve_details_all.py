import json
import os
from functools import lru_cache
from rest_framework.reverse import reverse
from django.conf import settings


class CVEDetailsAll:
    feeder_url = "https://raw.githubusercontent.com/pawlaczyk/sarenka_tools/master/cve_all.json"
    file_name = "cve_all.json"
    source_nist = "https://nvd.nist.gov/vuln/full-listing"
    nist_url = "https://nvd.nist.gov/vuln/detail/"
    mitre_cwe_url = "https://cwe.mitre.org/data/definitions/"
    file_prefix = "cve_all_details"
    feed_file_path = "feedes\cve_details\\"

    def __init__(self, page:str):
        self.__page = int(page)
        self.__filepath = self.get_filepath()
        self.__data = self.get_data()

    @property
    @lru_cache
    def values(self):
        return self.__data

    def get_filepath(self):
        two_up = os.path.abspath(os.path.join(settings.BASE_DIR, "../.."))
        feed_path = os.path.join(two_up, self.feed_file_path )

        start_idx = str(self.__page * 100)
        end_idx = str((self.__page + 1) * 100)
        file_name = f"{self.file_prefix}_{start_idx}_{end_idx}.json"
        print("file_name: ", file_name)

        if file_name in os.listdir(feed_path):
            return os.path.join(feed_path, file_name)

        return None

    def get_data(self):
        data = []
        if self.__filepath:
            with open(self.__filepath) as json_file:
                data = json.load(json_file)

        return data # zwraca w postaci jsona

    def render_output(self, host_address):
        """Dodaje url do sarenki i zewnętrzen do mitre wskazujące na mitre"""
        result = {}

        all_cves = self.values
        if all_cves:
            for cve in all_cves: #lista słowników
                cve_id = cve["cve_id"]

                cve["nist_cve_url"] = f"{self.nist_url}{cve_id}"
                cve["sarenka_cve_url"] = host_address + reverse('get_by_cve', kwargs={"cve_id": cve_id})

                if cve["cwe_id"]:
                    cwe_id = cve["cwe_id"].split("-")[-1]  # oólne np.: SQLi
                    cve["mitre_cwe_url"] = f"{self.mitre_cwe_url}{cwe_id}"
                    cve["sarenka_cwe_url"] = host_address + reverse('get_by_cwe', kwargs={"id_cwe": cwe_id})
                else:
                    cve["mitre_cwe_url"] = None
                    cve["sarenka_cwe_url"] = None

            return all_cves

        # jak nie ma danych
        return {"page": self.__page, "message": "No data available"}


