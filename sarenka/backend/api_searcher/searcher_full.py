"""
Moduł spiający wszystkie wyszukiwania w jedną klasę - wszystkei dane dla adresu ip/domeny.
Klasa bezpośrednio używana w widoku Django.
"""
from rest_framework.reverse import reverse
from typing import List, Dict
import whois
import socket

from connectors.credential import CredentialsNotFoundError
from api_searcher.search_engines.censys_engine.censys_host_search import CensysHostSearch
from api_searcher.search_engines.shodan_engine.shodan_host_search import ShodanHostSearch
from .dns.dns_searcher import DNSSearcher, DNSSearcherError


class SearcherFull:
    """Klasa zwracajaca wszystkie znalezione dane - zwraca infromacje ze wszystkich serwisów trzeich, informacje o DNS etc."""
    def __init__(self, ip_address:str, local_host_address="", user_credentials=None):
        self.host = ip_address
        self.host_address = local_host_address
        self.user_credentials = user_credentials

    def get_whois_data(self):
        """Metoda zwraca dane z bazy whois."""
        return whois.whois(self.host)

    def get_banner(self, port_list)->List[Dict]:
        """Metoda zwraca banery, które pórbuje uzyskac dla otwartych portów zwróconych przez seriwsy trzecie"""
        result = []
        for port in port_list:
            s = socket.socket()
            s.connect((self.host, int(port)))
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
        """Metoda zwraca dane wyszukane w serwisie http://censys.io/"""
        try:
            if not self.user_credentials:
                raise CredentialsNotFoundError("UserCredentials object does not exist.")

        except CredentialsNotFoundError as ex:
            settings_url = self.host_address + reverse('settings')
            return {
                "censys": {
                    "error": "Unable to get credentials for service http://censys.io/. "
                             "Please create account on https://censys.io/ and add valid settings "
                             f"for SARENKA app on {settings_url}",
                    "details": str(ex)
                    }
                }
        try:
            response = CensysHostSearch(self.user_credentials).response(self.host) #
            response.update({"banners": self.get_banner(response["ports"])})
            return response
        except Exception as ex:
            # censys nie udostępnia do importu klasy exceptionu CensysNotFoundException o.Ó
            return {
                "censys": {
                    "error": f"Unable to get infromation from https://censys.io/ service.",
                    "details": str(ex)
                    }
                }

    def get_shodan_data(self):
        """Metoda zwraca dane wyszukane w serwisie https://www.shodan.io/"""
        try:
            if not self.user_credentials:
                raise CredentialsNotFoundError("UserCredentials object does not exist.")

        except CredentialsNotFoundError as ex:
            settings_url = self.host_address + reverse('settings')
            return {
                "shodan": {
                    "error": "Unable to get credentials for service https://www.shodan.io/. "
                             "Please create account on https://www.shodan.io/ and add valid settings "
                             f"for SARENKA app on {settings_url}",
                    "details": str(ex)
                    }
                }
        try:
            response = ShodanHostSearch(self.user_credentials).response(self.host) #
            return response
        except Exception as ex:
            # censys nie udostępnia do importu klasy exceptionu CensysNotFoundException o.Ó
            return {
                "shodan": {
                    "error": f"Unable to get infromation from https://www.shodan.io/ service.",
                    "details": str(ex)
                    }
                }


    def get_dns_data(self):
        """Metoda zwraca informacje o rekordach DNS hosta."""
        try:
            data = DNSSearcher(self.host).get_data()
            return data
        except DNSSearcherError as ex:
            return {"error": str(ex)}
        except Exception as ex:
            return {"error": f"Unable to get DNS record data for host={self.host}.", "details": str(ex)}

    @property
    def values(self):
        """Zwraca jsona ze wszystkimi danymi - metoda pomocna dla widoków Django."""
        response = {
            "whois": self.get_whois_data(),
            "dns_data": self.get_dns_data(),
        }
        response.update({"censys": self.get_censys_data()})
        response.update({"shodan": self.get_shodan_data()})

        return response