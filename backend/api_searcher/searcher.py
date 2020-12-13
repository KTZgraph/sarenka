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
    def __init__(self, ip_address:str):
        self.ip_address = ip_address

    def get_whois_data(self):
        return whois.whois(self.ip_address)

    def get_censys_data(self):
        credentials = Credential().censys
        connector = CensysConnector(credentials)
        try:
            response = connector.search_by_ip(self.ip_address) #
            return response.to_json
        except BaseException:
            # censys nie udostępnia do importu klasy exceptionu CensysNotFoundException o.Ó
            return "Censys doesn't know anything about the specified host"


    @property
    def values(self):
        """Zwraca jsona ze wszystkimi danymi - metoda pomocna dla widoków Django."""
        response = {
            "whois": self.get_whois_data(),
            "dns": DNSSearcher(self.ip_address).values,
        }
        response.update(self.get_censys_data())

        return response