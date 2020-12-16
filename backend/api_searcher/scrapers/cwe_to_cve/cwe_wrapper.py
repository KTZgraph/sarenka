from typing import List

class CWEWrapper:
    def __init__(self, cwe, cve_list:List=[]):
        self.__cwe = cwe
        self.__cve_list = cve_list

    @property
    def cwe(self):
        return self.__cwe

    @cwe.setter
    def cwe(self, value):
        self.__cwe = value

    @cwe.deleter
    def cwe(self):
        self.__cwe = None

    @property
    def cve_list(self):
        return self.__cve_list

    @cwe.setter
    def cve_list(self, value):
        self.__cve_list = value

    @cwe.deleter
    def cve_list(self):
        self.__cve_list = None

