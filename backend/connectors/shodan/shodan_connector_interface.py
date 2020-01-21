from typing import Dict, Tuple, Sequence, List, NoReturn
from abc import ABC, abstractmethod


class ShodanConnectorInterface(ABC):
    def __init__(self, api_key:str)->None:
        self.api_key = api_key
    
    @abstractmethod
    def search(self, query:str)->List:
        """Search software by name"""
        pass

    @abstractmethod
    def host(self, ip, ports=[]):
        pass
