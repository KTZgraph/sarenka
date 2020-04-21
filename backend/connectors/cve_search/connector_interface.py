from typing import Dict, Tuple, Sequence, List, NoReturn
from abc import ABC, abstractmethod


class ConnectorInterface(ABC):
    def __init__(self, credentials):
        print(credentials)
        self.__base_url = credentials.base_url
        self.__cve = credentials.cve
        self.__vendor = credentials.vendor
        self.__last = credentials.last
        self.__db_info = credentials.db_info

    @property
    def base_url(self):
        return self.__base_url
    
    @property
    def vendor(self):
        return self.__vendor
    
    @property
    def cve(self):
        return self.__cve

    @property
    def db_info(self):
        return self.__db_info

    @property
    def last(self):
        return self.__last

    @abstractmethod
    def search_by_cve_code(self, cve_code):
        """
        curl https://cve.circl.lu/api/cve/CVE-2010-3333
        """
        pass

    @abstractmethod
    def get_last_30_cves(self):
        pass

    @abstractmethod
    def get_vendors_list(self):
        """
        curl https://cve.circl.lu/api/browse
        """
        pass

    @abstractmethod
    def get_vendor_products(self, vendor):
        """
        curl https://cve.circl.lu/api/browse/microsoft
        """
        pass

    @abstractmethod
    def get_product(self, vendor, product):
        """
        curl https://cve.circl.lu/api/search/microsoft/office
        """
        pass

    @abstractmethod
    def get_db_info(self):
        """
        curl https://cve.circl.lu/api/dbInfo
        """
        pass
