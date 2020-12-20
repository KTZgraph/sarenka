import json
import os
from functools import lru_cache
from rest_framework.reverse import reverse
from django.conf import settings


class CWEDetailsAll:
    source_nist = "https://nvd.nist.gov/vuln/full-listing"
    nist_url = "https://nvd.nist.gov/vuln/detail/"
    mitre_cwe_url = "https://cwe.mitre.org/data/definitions/"
    file_prefix = "cwe_details"
    feed_file_path = "feedes\cwe_details\\"

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
        feed_path = os.path.join(two_up, "feedes\cwe_details\\" )

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