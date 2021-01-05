import json
import requests
import os
from django.conf import settings
from functools import lru_cache
from rest_framework.reverse import reverse


class CWEAll:
    __feed_file_path = "feeds\\cwe_ids\\cwe_all.json"
    __file_name = "cwe_all.json"
    __source_cwe = "https://cwe.mitre.org/data/published/cwe_latest.pdf"
    __mitre_cwe_url = "https://cwe.mitre.org/data/definitions/" # np.: https://cwe.mitre.org/data/definitions/79.html

    def __init__(self):
        self.__data = self.get_data()

    @property
    @lru_cache
    def values(self):
        return self.__data

    def get_data(self):
        # pobiera dane z folderu feeds
        two_up = os.path.abspath(os.path.join(settings.BASE_DIR, "../.."))
        feed_path = os.path.join(two_up, self.__feed_file_path)

        with open(feed_path) as json_file:
            data = json.load(json_file)

        return data # zwraca w postaci jsona

    def render_output(self, host_address):
        """Dodaje url do sarenki i zewnętrzen do mitre wskazujące na mitre"""
        result = {}
        result.update({"created_at": self.values["created_at"]})
        result.update({"timestamp": self.values["timestamp"]})
        result.update({"source": self.__source_cwe})

        all_cwes = self.values["cwe_all"] #lista słowników
        for cwe in all_cwes:
            cwe_number = cwe["cwe_id"].split("-")[-1]
            cwe["mitre_url"] = f"{self.__mitre_cwe_url}{cwe_number}.html"
            cwe["sarenka_url"] = host_address + reverse('get_by_cwe', kwargs={"id_cwe": cwe["cwe_id"]})

        result.update({"cwe_all": all_cwes})

        return result
