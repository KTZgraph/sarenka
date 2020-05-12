from typing import Dict, Tuple, Sequence, List, NoReturn
from abc import ABC, abstractmethod

class AnalyzerInterface(ABC):
    __name = "" # atrybut klasy nazwa analizowanego softu

    @abstractmethod
    def get_all_cves(self):
        pass

    @abstractmethod
    def regex_pattern(self, regex_file="version_regexs.json"):
        pass

    @abstractmethod
    def sort_by_version(self):
        pass

    @abstractmethod
    def save_results(self):
        pass