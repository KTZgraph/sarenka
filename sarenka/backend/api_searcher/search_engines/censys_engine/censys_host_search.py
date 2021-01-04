from .censys_credentials import CensysCredentials,CensysCredentialsError
from .censys_connector import CensysConnector


class CensysHostSearchError(Exception):
    """
    Zgłoszenie wyjąktu gdy nie można pobrac danych z serwisu censys.io.
    """
    def __init__(self, message=None, errors=None):
        super().__init__(message)
        self.errors = errors


class CensysHostSearch:
    """Klasa zwraca dane z wyszukiwarki censysa dla widoków Django"""
    def __init__(self, user_credentials):
        self.user_credentials = user_credentials


    def response(self, ip_address):
        """Zwraca dane w formie jsona dla widoku Django"""
        try:
            censys_credentials = self.user_credentials.censys
            connector = CensysConnector(censys_credentials)
            response = connector.search_by_ip(ip_address)
            return response.to_json # TODO zmienić na serializatory
        except CensysCredentialsError as ex:
            raise CensysHostSearchError("Invalid settings for service https://censys.io/. " + str(ex))

