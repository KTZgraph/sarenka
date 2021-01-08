from censys.certificates import CensysCertificates
from censys.ipv4 import CensysIPv4
from censys.websites import CensysWebsites
from .wrappers.ip_wrapper import IPWrapper


class CensysConnectorError(Exception):
    """Zgłasza wyjątek gdy nie można pobrać danych z serwisu https://censys.io/."""
    def __init__(self, message=None, errors=None):
        super().__init__(message)
        self.errors = errors


class CensysConnector:
    """Klasa konektora odopowiadająca za pobieranie danych z serwisu https://censys.io/."""
    def __init__(self, credentials):
        self.__ipv4 = CensysIPv4(api_id=credentials.api_id, api_secret=credentials.secret)
        self.__certificate = CensysCertificates(api_id=credentials.api_id, api_secret=credentials.secret)
        self.__websites = CensysWebsites(api_id=credentials.api_id, api_secret=credentials.secret)

    @property
    def ipv4(self):
        return self.__ipv4

    @property
    def certificate(self):
        return self.__certificate

    @property
    def website(self):
        return self.__websites

    def search_by_ip(self, ip):
        """
        Metoda szukająca infromacji o hoście na podtawie jego adresu ip z serwisu https://censys.io/..
        Np.:https://censys.io/ipv4/150.254.78.51
        """
        response = self.ipv4.view(ip)
        return IPWrapper(response)

    def search_by_fingerprint(self, certificate_hash):
        return self.certificate.view(certificate_hash)

    def search_by_website(self, domain):
        return self.website.view(domain)

