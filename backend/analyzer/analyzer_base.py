from typing import Dict, Tuple, Sequence, List, NoReturn
from collections import namedtuple
import re

from analyzer.analyzer_interface import AnalyzerInterface
from analyzer.softwares.software_info_interface import SoftwareInfoInterface
from analyzer.softwares.imagemagick import ImageMagick
from connectors.credential import Credential
from connectors.cve_search.connector import Connector as CVESearchApi
from common.text_parser import TextParser
from common.common import Common

CVEVersion = namedtuple("CVEVersion", "code summary version")


class AnalyzerBase(AnalyzerInterface):
    connector = CVESearchApi(Credential().cve_search)

    def __init__(self, software_info:SoftwareInfoInterface):
        self.info = software_info

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

    @classmethod
    def get_url_data(cls, cve):
        cve_wrapper = cls.connector.search_by_cve_code(cve)
        return cve_wrapper

    def get_summary(self, data):
        result = []
        cve_list = Common.parse_to_list(data)
        SoftwareCVE = namedtuple(self.info.name, 'cve summary match')

        for cve in cve_list:
            cve_wrapper = AnalyzerBase.get_url_data(cve)

            result.append(
                SoftwareCVE(
                    cve, 
                    cve_wrapper.summary, 
                    self.__find_version(cve_wrapper.summary)
                )
            )

        return result

    @staticmethod
    def __sort_dict_list_by_attribute(dict_list, key_name="version"):
        dict_list.sort(key=itemgetter(key_name), reverse=False)
        return dict_list


    @staticmethod
    def get_versions_from_dict(dict_list):
        all_version = Common.list_flattening([d.version for d in dict_list])
        all_version_unique = list(set(all_version))
        all_version_unique.sort()
        return all_version_unique

    def convert_to_version_cve_dict(self, data):
        dict_list = AnalyzerBase.sort_by_version(data)
        all_versions = AnalyzerBase.get_versions_from_dict(dict_list)
        result = {version: [] for version in all_versions}
        for d in dict_list:
            for version in d.version:
                result[version].append({d.code: d.summary})
        return result

    @staticmethod
    def sort_by_version(data):
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


    def __find_version(self, summary):
        if summary:
            match = re.findall(self.info.pattern,  summary)
            return AnalyzerBase.__clean_match(match)
        return [None]

    @staticmethod
    def save_to_file(fileoutput, sorted_by_version): #TODO mniej pozszywane/zagnieżdzoen te obiekty wersji
        result = {}
        for version_no in sorted_by_version.keys():
            for cve_data in sorted_by_version[version_no]:
                for cve_keys in cve_data:
                    cve_key = list(cve_data.keys())[0]
                    result[version_no] = {cve_key : cve_data[cve_key]} 

        Common.save_dict_to_file(fileoutput, result)

if __name__ == "__main__":
    filename = "C:\\Users\\dp\Desktop\\sarenka\\backend\\analyzer\\imagemagic_cve.txt"
    list_cves = TextParser().get_cve_list_from_file(filename)
    image_magick = ImageMagick()
    analyzer_base = AnalyzerBase(image_magick)
