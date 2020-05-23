import re

from common.common import Common


class TextParser:

    @staticmethod
    def read_file_with_cves(filename):
        output = []
        with open(filename, "r") as f:
            for line in f.readlines():
                if line != "\n":
                    output.append(line)
        
        return output

    @staticmethod
    def get_unique_list(flat_list):
        l = list(set(flat_list))
        l.sort()
        return l

    @staticmethod
    def __find_cve_code(line):
        match = re.findall(r"CVE\-\d{4}\-\d+", line)
        return match

    @staticmethod
    def get_cve_list_from_file(filename):
        output = TextParser.read_file_with_cves(filename)
        matches = []
        not_analyzed = [] #błedy co się nie udało # TODO: logger
        for line in output:
            try:
                match = TextParser.__find_cve_code(line)
                if match:
                    matches.append(match)
            except BaseException as ex:
                not_analyzed.append(line) # TODO: logger

        
        flat_list = Common.list_flattening(matches)
        print("NOT ANALYZED: ", not_analyzed)

        return TextParser.get_unique_list(flat_list)

    @staticmethod
    def save_cve_list(cve_flat_list, software_name):
        filename = software_name+"_cve.txt"
        Common.save_list_to_file(filename, cve_flat_list, separator="\n")

