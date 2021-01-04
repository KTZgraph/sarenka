import shodan

from .wrappers.host_details_wrapper import HostDetailsWrapper
from .wrappers.host_wrapper import HostWrapper


class ShodanConnectorError(Exception):
    """Zgłasza wyjątek gdy nie można pobrać danych z serwisu https://shodan.io/"""
    def __init__(self, message=None, errors=None):
        super().__init__(message)
        self.errors = errors


class ShodanConnector:
    """Klasa konektora odopowiadająca za pobieranie danych z serwisu https://www.shodan.io/."""
    def __init__(self, credentials):
        self.__base_url = credentials.base_url
        self.__api_key = credentials.api_key
        self.__user = credentials.user
        self.__connector = shodan.Shodan(self.__api_key)

    def search_by_ip(self, ip_address):
        """
        Metoda szukająca infromacji o hoście na podtawie jego adresu ip z serwisu https://www.shodan.io/.
        Np.: https://www.shodan.io/host/150.254.78.51
        """
        result = self.__connector.host(ip_address)
        return HostDetailsWrapper(ip_address, result)

    def search_by_asn(self, asn):
        """
        NIE DOSTĘPNA W TEJ WERSJI
        https://www.shodan.io/search?query=asn%3AAS6846
        w censysie numer asn jest widoczny - punkt spięcia wyszukiwań
        z censysa "autonomous_system": {"description": "GOOGLE", "rir": "unknown", "routed_prefix": "8.8.8.0/24", "country_code": "US", "path": [15169], "asn": 15169, "name": "GOOGLE"},
        """
        raise NotImplementedError("ShodanConnector().search_by_asn")

    def search_by_technology_name(self, query, amount=3) -> [HostWrapper]:
        """
        METODA NIE DOSTĘPNA W TEJ WERSJI
        :param query: 
        :param amount: 
        :return: 
        """
        # hosts = []
        # try:
        #     results = self.api.search(query)
        #     for result in results['matches'][0:amount]:
        #         host = HostWrapper(result, query)
        #         hosts.append(host)
        #
        # except shodan.APIError as exception:
        #     print('Error: {}'.format(exception))
        # finally:
        #     return hosts
        raise NotImplementedError("ShodanConnector().search_by_technology_name")
