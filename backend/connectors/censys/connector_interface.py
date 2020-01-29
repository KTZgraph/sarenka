from typing import Dict, Tuple, Sequence, List, NoReturn
from abc import ABC, abstractmethod


class ConnectorInterface(ABC):
    def __init__(self, data):
        self.__base_url = data.base_url
        self.__api_id = data.api_id
        self.__secret = data.secret
        self.__api_url = data.api_url

    @property
    def base_url(self):
        return self.__base_url
    
    @property
    def api_id(self):
        return self.__api_id
    
    @property
    def secret(self):
        return self.__secret

    @property
    def api_url(self):
        return self.__api_url

    @abstractmethod
    def host(self, ip, ports=[]):
        pass
