from connectors.credential import Credential, CredentialsNotFoundError
from connectors.censys.connector import Connector as CensysConnector


class CensysHostSearchError(Exception):
    """
    Zgłoszenie wyjąktu gdy nie można pobrac danych z serwisu censys.io.
    """
    def __init__(self, message=None, errors=None):
        super().__init__(message)
        self.errors = errors


class CensysHostSearch:
    """Klasa zwraca dane z wyszukiwarki censysa dla widoków Django"""
    @staticmethod
    def response(ip_address):
        """Zwraca dane w formie jsona dla widoku Django"""
        try:
            credentials = Credential().censys
            connector = CensysConnector(credentials)
            response = connector.search_by_ip(ip_address)
            return response.to_json # TODO zmienić na serializatory
        except CredentialsNotFoundError:
            raise CensysHostSearchError("Invalid settings for service https://censys.io/")

