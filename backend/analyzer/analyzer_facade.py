from typing import Dict, Tuple, Sequence, List, NoReturn

from analyzer.softwares.software_info_interface import SoftwareInfoInterface
from analyzer.analyzer_base import AnalyzerBase
from analyzer.softwares.imagemagick import ImageMagick
from common.text_parser import TextParser
from common.common import Common


class AnalyzerFacade:

    def __init__(self, software_info:SoftwareInfoInterface):
        self.analyzer = AnalyzerBase(software_info)

    def save_to_file(self, fileoutput, sorted_by_version):
        filename = fileoutput.split(".")[0] + "_all." + fileoutput.split(".")[1]
        self.analyzer.save_to_file(filename, sorted_by_version)

    def version_data_from_list(self, list_cves):
        summary = self.analyzer.get_summary(list_cves)
        sorted_by_version = self.analyzer.convert_to_version_cve_dict(summary)
        return sorted_by_version

    def version_data_from_file(self, filename, files_save=True, fileoutput="sorted.json"):
        list_cves = TextParser().get_cve_list_from_file(filename)
        sorted_by_version = self.version_data_from_list(list_cves)

        if files_save:
            self.save_to_file(fileoutput, sorted_by_version)

        return sorted_by_version


if __name__ == "__main__":
    file_with_cves = "C:\\Users\\dp\Desktop\\sarenka\\backend\\analyzer\\imagemagic_cve.txt"
    image_magick = ImageMagick()
    analyzer_facade = AnalyzerFacade(image_magick)
    sorted_by_version = analyzer_facade.version_data_from_file(filename=file_with_cves)
    print(sorted_by_version)