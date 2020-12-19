import json
import requests
import os
from functools import lru_cache


class CWEAll:
    feeder_url = "https://raw.githubusercontent.com/pawlaczyk/sarenka_tools/master/cwe_all.json"
    file_name ="cwe_all.json"

    def __init__(self):
        self.__data = self.get_data()

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

        with open("cwe_all.json") as json_file:
            data = json.load(json_file)

        return data # zwraca w postaci jsona

    @property
    @lru_cache
    def values(self):
        return self.__data
