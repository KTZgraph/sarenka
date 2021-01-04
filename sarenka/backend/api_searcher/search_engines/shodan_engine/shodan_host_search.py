from .shodan_credentials import ShodanCredentialsError
from .shodan_connector import ShodanConnector


class ShodanHostSearchError(Exception):
    """
    Zgłoszenie wyjąktu gdy nie można pobrac danych z serwisu https://shodan.io/".
    """
    def __init__(self, message=None, errors=None):
        super().__init__(message)
        self.errors = errors


class ShodanHostSearch:
    """Klasa zwraca dane z serwisu https://shodan.io/" dla widoków Django"""
    def __init__(self, user_credentials):
        self.user_credentials = user_credentials


    def response(self, ip_address):
        """Zwraca dane w formie jsona dla widoku Django"""
        try:
            shodan_credentials = self.user_credentials.shodan
            connector = ShodanConnector(shodan_credentials)
            response = connector.search_by_ip(ip_address)
            return response.to_json # TODO zmienić na serializatory
        except ShodanHostSearchError as ex:
            raise ShodanHostSearchError("Invalid settings for service https://censys.io/. " + str(ex))
