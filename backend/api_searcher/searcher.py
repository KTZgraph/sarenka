"""
Moduł spiający wszystkie wyszukiwania w jedną klasę - wszystkei dane dla adresu ip/domeny.
Klasa bezpośrednio używana w widoku Django.
"""
import whois
from connectors.credential import Credential
from connectors.cve_search.connector import Connector as CVEConnector
from connectors.censys.connector import Connector as CensysConnector
from .dns.dns_searcher import DNSSearcher


class Searcher:
    def __init__(self, host):
        self.host = host
        self.ip_address = Searcher.get_host_ip_address(host)

    @staticmethod
    def get_host_ip_address(host):
        return host

    def get_whois_data(self):
        return whois.whois(self.host)

    def censys_data(self):
        credentials = Credential().censys
        connector = CensysConnector(credentials)
        return connector.search_by_ip(self.ip_addres) #


    @property
    def values(self):
        """Zwraca jsona ze wszystkimi danymi - metoda pomocna dla widoków Django."""
        return {
            "searcher" :"dane ze wszystkich wyszukiwarek",
            "whois": self.get_whois_data(),
            "dns": DNSSearcher(self.host).values
        }