import requests
from operator import itemgetter
import re
import json

from .analyzer_interface import AnalyzerInterface
from common.text_parser import TextParser
from common.common import Common

class ImageMagick:
    def __init__(self, data):
        self.api = "https://cve.circl.lu/api/cve/"
        self.__cve_list = self.parse_to_list(data)
        self.__summary = self.get_summary()

    @property
    def cve_list(self):
        return self.__cve_list

    @property
    def summary(self):
        return self.__summary

    @staticmethod
    def parse_to_list(data):

        if isinstance(data, list):
            output = data

        if isinstance(data, str):
            with open(data, "r") as f:
                output = f.readlines()
            output = [i.rstrip() for i in output]

        return output

    def __clean_match(self, one_cve_matches):
        founded = [None]
        matches = [list(i) for i in one_cve_matches]
        match = Common.list_flattening(matches)
        if one_cve_matches:
            founded = [m for m in match if m]

        return founded

    def __find_version(self, summary):
        if summary:
            match = re.findall(r"(before\s+and\s+\d+\.\d+\.\d+\-\d+( Q16)?)|(before\s+\d+\.\d+\.\d+\-\d+( Q16)?)|(\d+\.\d+\.\d+\-\d+( Q16)?\s+and\s+earlier)|(\d+\.\d+\.\d+\-\d+( Q16)?)|(before\s+\d+\.\d+\.\d+( Q16)?)|(\d+\.\d+\.\d+( Q16)?\s+and\s+earlier)|(\d+\.\d+\.\d+( Q16)?)", summary)
            return self.__clean_match(match)
        return [None]

    def get_url_data(self, cve):
        url = f'{self.api}{cve}'
        status = 0
        while status != 200:
            response = requests.get(url)
            status = response.status_code

        return response.json()

    def get_summary(self):
        result = []
        for cve in self.cve_list:
            response = self.get_url_data(cve)

            summary = response.get("summary") #TODO: wrapper
            result.append({
                "cve": cve,
                "summary": summary,
                "match": self.__find_version(summary)
            })

        return result

    @staticmethod
    def sort_dict_list_by_attribute(dict_list, key_name="version"):
        dict_list.sort(key=itemgetter(key_name), reverse=False)
        return dict_list

    @staticmethod
    def get_versions_from_dict(dict_list):
        all_version = Common.list_flattening([d["version"] for d in dict_list])
        all_version_unique = list(set(all_version))
        all_version_unique.sort()
        return all_version_unique

    @staticmethod
    def convert_to_version_cve_dict(dict_list):
        all_versions = ImageMagick.get_versions_from_dict(dict_list)
        result = {version: [] for version in all_versions}
        for d in dict_list:
            for version in d["version"]:
                result[version].append(d["cve"])
        return result

    @staticmethod
    def sort_by_version(data):
        dict_list_sorted = []
        for d in data:
            version = [i for i in d["match"] if i != " Q16"]
            minimal_data = {"cve": {"code": d["cve"], "summary": d["summary"]}, "version": version, }
            dict_list_sorted.append(minimal_data)

        return dict_list_sorted


class ImageMagickFacade:
    @staticmethod
    def __save_files(fileoutput, sorted_by_version):
        filename = fileoutput.split(".")[0] + "_all." + fileoutput.split(".")[1]
        Common.save_dict_to_file(filename, sorted_by_version)

        result = {}
        for k in sorted_by_version.keys():
            result[k] = [i["code"] for i in sorted_by_version[k]]

        Common.save_dict_to_file(fileoutput, result)
    
    @staticmethod
    def version_data_from_list(list_cves):
        image_magick_cve = ImageMagick(list_cves)
        summary = image_magick_cve.summary
        dict_list_sorted = ImageMagick.sort_by_version(summary)
        sorted_by_version = ImageMagick.convert_to_version_cve_dict(dict_list_sorted)
        return sorted_by_version

    @staticmethod
    def version_data_from_file(filename, files_save=True, fileoutput="sorted.json"):
        list_cves = TextParser().get_cve_list_from_file(filename)
        sorted_by_version = ImageMagickFacade.version_data_from_list(list_cves)

        if files_save:
            ImageMagickFacade.__save_files(fileoutput, sorted_by_version)

        return sorted_by_version

if __name__ == "__main__":
    file_with_cves = "imagemagic_cve.txt"
    sorted_by_version = ImageMagickFacade.version_data_from_file(filename=file_with_cves)