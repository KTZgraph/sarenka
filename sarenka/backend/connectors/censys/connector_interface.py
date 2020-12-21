from typing import Dict, Tuple, Sequence, List, NoReturn
from abc import ABC, abstractmethod
from censys.ipv4 import CensysIPv4
from censys.certificates import CensysCertificates
from censys.websites import CensysWebsites
from censys.base import CensysNotFoundException, CensysRateLimitExceededException, CensysUnauthorizedException


class ConnectorInterface(ABC):
    def __init__(self, data):
        self.__ipv4 = CensysIPv4(api_id=data.api_id, api_secret=data.secret)
        self.__certificate = CensysCertificates(api_id=data.api_id, api_secret=data.secret)
        self.__websites = CensysWebsites(api_id=data.api_id, api_secret=data.secret)

    @property
    def ipv4(self):
        return self.__ipv4
    
    @property
    def certificate(self):
        return self.__certificate
    
    @property
    def website(self):
        return self.__websites

    @abstractmethod
    def search_by_ip(self, ip):
        pass

    @abstractmethod
    def search_by_fingerprint(self, certificate_hash):
        pass

    @abstractmethod
    def search_by_website(self, domain):
        pass
