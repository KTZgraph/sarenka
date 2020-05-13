import requests
from operator import itemgetter
import re
import json
from collections import namedtuple

from .analyzer_interface import AnalyzerInterface
from common.text_parser import TextParser
from common.common import Common
from connectors.credential import Credential
from connectors.cve_search.connector import Connector as CVESearchApi


ImageMagickCVE = namedtuple('ImageMagickCVE', 'cve summary match')
CVEVersion = namedtuple("CVEVersion", "code summary version")


class ImageMagick:
    __github = "https://github.com/ImageMagick/ImageMagick/"
    connector = CVESearchApi(Credential().cve_search)

    @staticmethod
    def parse_to_list(data):

        if isinstance(data, list):
            output = data

        if isinstance(data, str):
            with open(data, "r") as f:
                output = f.readlines()
            output = [i.rstrip() for i in output]

        return output

    @staticmethod
    def __clean_match(one_cve_matches):
        founded = [None]
        matches = [list(i) for i in one_cve_matches]
        match = Common.list_flattening(matches)
        if one_cve_matches:
            founded = [m for m in match if m]
        if not founded:
            return ["null"]

        return founded

    @staticmethod
    def __find_version(summary):
        if summary:
            match = re.findall(r"(before\s+and\s+\d+\.\d+\.\d+\-\d+( Q16)?)|(before\s+\d+\.\d+\.\d+\-\d+( Q16)?)|(\d+\.\d+\.\d+\-\d+( Q16)?\s+and\s+earlier)|(\d+\.\d+\.\d+\-\d+( Q16)?)|(before\s+\d+\.\d+\.\d+( Q16)?)|(\d+\.\d+\.\d+( Q16)?\s+and\s+earlier)|(\d+\.\d+\.\d+( Q16)?)", summary)
            return ImageMagick.__clean_match(match)
        return [None]

    @classmethod
    def get_url_data(cls, cve):
        cve_wrapper = cls.connector.search_by_cve_code(cve)
        return cve_wrapper

    @staticmethod
    def get_summary(data):
        result = []
        cve_list = ImageMagick.parse_to_list(data)
        for cve in cve_list:
            cve_wrapper = ImageMagick.get_url_data(cve)

            result.append(
                ImageMagickCVE(
                    cve, 
                    cve_wrapper.summary, 
                    ImageMagick.__find_version(cve_wrapper.summary)
                )
            )

        return result

    @staticmethod
    def sort_dict_list_by_attribute(dict_list, key_name="version"):
        dict_list.sort(key=itemgetter(key_name), reverse=False)
        return dict_list

    @staticmethod
    def get_versions_from_dict(dict_list):
        all_version = Common.list_flattening([d.version for d in dict_list])
        all_version_unique = list(set(all_version))
        all_version_unique.sort()
        return all_version_unique

    def convert_to_version_cve_dict(data):
        dict_list = ImageMagick.__sort_by_version(data)
        all_versions = ImageMagick.get_versions_from_dict(dict_list)
        result = {version: [] for version in all_versions}
        for d in dict_list:
            for version in d.version:
                result[version].append({d.code: d.summary})
        return result

    @staticmethod
    def __sort_by_version(data):
        dict_list_sorted = []
        for d in data:
            version = [i for i in d.match if i != " Q16"] #specific for imageMagic
            dict_list_sorted.append(
                CVEVersion(
                    d.cve, 
                    d.summary,
                    version
                )
            )

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
        summary = ImageMagick.get_summary(list_cves)
        sorted_by_version = ImageMagick.convert_to_version_cve_dict(summary)
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