from typing import Dict, Tuple, Sequence, List, NoReturn
from abc import ABC, abstractmethod

class AnalyzerInterface(ABC):
    """
    UWAGA:
    https://stackoverflow.com/questions/4474395/staticmethod-and-abc-abstractmethod-will-it-blend
    That a method is static controls how it is called. An abstract method is never called. And abstract static method is therefore a pretty pointless concept, except for documentation purposes
    @dlatego nie używam abstractmethod ale zostawiam interfejsy bo nieograniemy takiej ilości kodu
    """

    @staticmethod
    def __parse_to_list(data):
        pass

    @staticmethod
    def __clean_match(one_cve_matches):
        pass

    @abstractmethod
    def get_summary(self, data):
        """
        Pobiera dane z cve-details - opis oprogramowania
        """
        pass

    @staticmethod
    def __sort_dict_list_by_attribute(dict_list, key_name="version"):
        pass

    @staticmethod
    def __get_versions_from_dict(dict_list):
        pass

    @abstractmethod
    def convert_to_version_cve_dict(self, data):
        pass

    @abstractmethod
    def sort_by_version(self, data):
        pass
