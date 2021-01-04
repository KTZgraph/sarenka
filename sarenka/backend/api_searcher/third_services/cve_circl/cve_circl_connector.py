"""
Moduł odpowiadający za połączenie i zbieranie danych od serwisu https://cve.circl.lu/.
"""
import requests

from .wrappers.cve_wrapper import CveWrapper


class CveCirclConnectorError(Exception):
    """
    Zgłasza wyjątek gdy nie można połaczyć się z serwisem https://cve.circl.lu/.
    """
    def __init__(self, message=None, errors=None):
        super().__init__(message)
        self.errors = errors


class CveCirclConnector:
    """Klasa będąca konektorem do serwisu trzeciego https://cve.circl.lu/."""
    def __init__(self, service_details):
        self.__base_url = service_details.base_url
        self.__cve = service_details.cve
        self.__vendor = service_details.vendor
        self.__last = service_details.last
        self.__db_info = service_details.db_info

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

    @staticmethod
    def connect(url):
        """Metoda pomocnicza klasy odpowidająca za rzadzanie GET HTTP do podanego urlu"""
        response = requests.get(url)
        if response.ok:
            return response.json()
        else:
            raise CveCirclConnectorError(f"Can't get data from {url}")

    def get_vendors_list(self):
        """Metoda zwracająca listę dostawców oprogramowania."""
        try:
            response = CveCirclConnector.connect(self.vendor)
            return response['vendor']
        except Exception as ex:
            raise CveCirclConnectorError(str(ex))

    def get_vendor_products(self, vendor:str):
        """Metoda zwracająca listę produktów dla danego dostawcy"""
        try:
            url = f'{self.vendor}{vendor}/'
            return requests.get(url)
        except Exception as ex:
            raise CveCirclConnectorError(str(ex))

    def get_product(self, vendor:str, product:str):
        """Metoda zwracająca informacje o oprogramowaniu na
        podstawie podanego dostawcy i nazwy produktu od użytkownika"""
        try:
            url = f'{self.vendor}{vendor}/{product}'
            return requests.get(url)
        except Exception as ex:
            raise CveCirclConnectorError(str(ex))

    def get_db_info(self:str):
        """Metoda zwraca infromacje o bazie danych serwisu https://cve.circl.lu/"""
        try:
            return requests.get(self.db_info)
        except Exception as ex:
            raise CveCirclConnectorError(str(ex))

    def search_by_cve_code(self, cve_code:str):
        """Metoda zwracająca informacje o podatności Common Vulnerabilities and Exposures CVE
        z serwisu https://cve.circl.lu/"""
        try:
            url = f'{self.cve}{cve_code}'
            response = CveCirclConnector.connect(url)
            cve_wrapper = CveWrapper(response)
            return cve_wrapper
        except Exception as ex:
            raise CveCirclConnectorError(str(ex))


