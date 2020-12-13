"""
Moduł spiający wszystkie wyszukiwania w jedną klasę - wszystkei dane dla adresu ip/domeny.
Klasa bezpośrednio używana w widoku Django.
"""
from typing import List, Dict
import whois
import socket

from connectors.credential import Credential
from connectors.cve_search.connector import Connector as CVEConnector
from connectors.censys.connector import Connector as CensysConnector
from .dns.dns_searcher import DNSSearcher


class Searcher:
    def __init__(self, ip_address:str):
        self.ip_address = ip_address

    def get_whois_data(self):
        return whois.whois(self.ip_address)

    def get_banner(self, port_list)->List[Dict]:
        """Pobieranie banera"""
        result = []
        for port in port_list:
            s = socket.socket()
            s.connect((self.ip_address, int(port)))
            s.settimeout(5)
            try:
                # jak nie ma banera to rzuca timeotam
                response = s.recv(1024)
                if response:
                    result.append({port: response})
            except socket.timeout:
                result.append({port: "Unable to grab banner."})

        return result

    def get_censys_data(self):
        credentials = Credential().censys
        connector = CensysConnector(credentials)
        try:
            response = connector.search_by_ip(self.ip_address).to_json #
            response.update({"banners": self.get_banner(response["ports"])})
            return response
        except BaseException as ex:
            print(ex)
            print(type(ex))

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