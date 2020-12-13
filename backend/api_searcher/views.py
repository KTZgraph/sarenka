from rest_framework import views
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import logging
import ipaddress
import socket

from connectors.credential import Credential
from connectors.cve_search.connector import Connector as CVEConnector
from connectors.censys.connector import Connector as CensysConnector
from .scrapers.mitre_cwe_scrapers import CWETableTop25Scraper, CWEDataScraper
from .scrapers.nist_cve_scrapers import  NISTCVEScraper
from .dns.dns_searcher import DNSSearcher, DNSSearcherFQDNError
from common.contact import Contact
from .windows.registry import WindowsRegistry
from .windows.hardware import Hardware
from .windows.network import LocalNetworkData
from .searcher import Searcher


logger = logging.getLogger('django')


class CVESearchView(views.APIView):
    def get_server_address(self, request):
        """
        Zwraca adres do serwera aplikacji z uwzglednieniem protokołu np: http://127.0.0.1:8000/.
        Użycie - generpowanie urli do wewnątrz aplikacji.
        """
        host_address = request.get_host()
        # TODO: refaktor
        if request.is_secure():
            address = "https://" + host_address
        else:
            address = "http://"+ host_address
        return address

    def get(self, request, code):
        """
        Zwraca infromacje o konkrentje podatności po id CVE

        """
        print("CVESearchView")
        logger.debug("Logger at CVESearchView test message")
        logger.warning("Logger at CVESearchView test message")
        logger.info("Logger at CVESearchView test message")
        logger.error("Logger at CVESearchView test message")
        """
        credentials = Credential().cve_search
        connector = CVEConnector(credentials)
        cve = connector.search_by_cve_code(code)
        response = CveWrapperSerializer(instance=cve).data
        return Response(response)
        """
        server_address = self.get_server_address(request)
        nist_cve_scraper = NISTCVEScraper(code, server_address)
        return Response(nist_cve_scraper.get_data())


class CWETop25(APIView):
    def get_server_address(self, request):
        """
        Zwraca adres do serwera aplikacji z uwzglednieniem protokołu np: http://127.0.0.1:8000/.
        Użycie - generpowanie urli do wewnątrz aplikacji.
        """
        host_address = request.get_host()
        # TODO: refaktor
        if request.is_secure():
            address = "https://" + host_address
        else:
            address = "http://"+ host_address
        return address

    def get(self, request):
        """
        Widok - zwraca informacje o TOP 25 najgroźniejszych słabościach oprogramowania
        """
        server_address = self.get_server_address(request)
        return Response({"response": CWETableTop25Scraper(server_address).get_top_25()})


class CWEData(APIView):
    """
    Zwraca infromacje o Common Weakness Enumeration na podstawie podane numeru CWE ID.
    http://127.0.0.1:8000/cwe/79
    http://127.0.0.1:8000/cwe/CWE-79
    http://127.0.0.1:8000/cwe/cwe-79

    """
    def get_server_address(self, request):
        """
        Zwraca adres do serwera aplikacji z uwzglednieniem protokołu np: http://127.0.0.1:8000/.
        Użycie - generpowanie urli do wewnątrz aplikacji.
        """
        host_address = request.get_host()
        # TODO: refaktor
        if request.is_secure():
            address = "https://" + host_address
        else:
            address = "http://"+ host_address
        return address

    def get(self, request, id_cwe):
        server_address = self.get_server_address(request)
        return Response(CWEDataScraper(server_address, id_cwe).get_data())


class CWETop25(APIView):
    def get_server_address(self, request):
        """
        Zwraca adres do serwera aplikacji z uwzglednieniem protokołu np: http://127.0.0.1:8000/.
        Użycie - generpowanie urli do wewnątrz aplikacji.
        """
        host_address = request.get_host()
        # TODO: refaktor
        if request.is_secure():
            address = "https://" + host_address
        else:
            address = "http://"+ host_address
        return address

    def get(self, request):
        """
        Widok - zwraca informacje o TOP 25 najgroźniejszych słabościach oprogramowania
        """
        server_address = self.get_server_address(request)
        return Response({"response": CWETableTop25Scraper(server_address).get_top_25()})


class CWEData(APIView):
    """
    Zwraca infromacje o Common Weakness Enumeration na podstawie podane numeru CWE ID.
    http://127.0.0.1:8000/cwe/79
    http://127.0.0.1:8000/cwe/CWE-79
    http://127.0.0.1:8000/cwe/cwe-79

    """
    def get_server_address(self, request):
        """
        Zwraca adres do serwera aplikacji z uwzglednieniem protokołu np: http://127.0.0.1:8000/.
        Użycie - generpowanie urli do wewnątrz aplikacji.
        """
        host_address = request.get_host()
        # TODO: refaktor
        if request.is_secure():
            address = "https://" + host_address
        else:
            address = "http://"+ host_address
        return address

    def get(self, request, id_cwe):
        server_address = self.get_server_address(request)
        return Response(CWEDataScraper(server_address, id_cwe).get_data())


class SearcherView(views.APIView):
    """
    Klasa zwrcająca dane o szukanym hoście po podanej domenie lub adresie ip.
    """
    def is_ipv4(self, host):
        try:
            ipaddress.IPv4Network(host)
            return True
        except ValueError:
            return False

    def change_to_domain_addres(self, host):
        if self.is_ipv4(host):
            return host
        return socket.gethostbyname(host)

    def get(self, request, host):
        """

        :param request:
        :param host: string mający adres ip lub domenę np.: python.org
        :return:
        """
        ip_address = self.change_to_domain_addres(host)
        return Response(Searcher(ip_address).values)


class CensysHostSearchView(views.APIView):
    # TODO refaktor !
    """
    Wyszukiwanie danych po IP
    opakowane protokoyły:
        - DNS
        - HTTPS
        - TLS
        - ataki "heartbleed", "logjam_attack", "freak_attack", "poodle_attack"
    """
    def get(self, request, ip_address):
        credentials = Credential().censys
        connector = CensysConnector(credentials)
        response = connector.search_by_ip(ip_address) #
        return Response(response.to_json)


class ListVendors(views.APIView):
    def get(self, request):
        credentials = Credential().cve_search
        connector = CVEConnector(credentials)
        listVendors = connector.get_vendors_list()
        return Response(listVendors)


class DNSSearcherView(APIView):

    def get(self, request, host='renmich.faculty.wmi.amu.edu.pl'):
        """
        Gets DNS A Record Data

        :param request: django request object
        :param host: fully qualified domain name
        :return: dns data
        :example: fqdn='renmich.faculty.wmi.amu.edu.pl'
        """
        data = DNSSearcher(host).values
        return Response(data)


class CrtShView(APIView):
    service = "https://crt.sh"
    repository = "https://github.com/crtsh/certwatch_db"

    def get(self, identity):
        """
        Identity (Domain Name, Organization Name, etc),
        a Certificate Fingerprint (SHA-1 or SHA-256) or a crt.sh ID:
        """
        url = f"{CrtShView.service}/?q={identity}"
        # https://crt.sh/?q=google.pl
        return JsonResponse({"CrtSh" : "Returns data from crt_sh_s"})


class CrtShView(APIView):
    service = "https://crt.sh"
    repository = "https://github.com/crtsh/certwatch_db"

    def get(self, identity):
        """
        Identity (Domain Name, Organization Name, etc),
        a Certificate Fingerprint (SHA-1 or SHA-256) or a crt.sh ID:
        """
        url = f"{CrtShView.service}/?q={identity}"
        # https://crt.sh/?q=google.pl
        return JsonResponse({"CrtSh" : "Returns data from crt_sh_s"})


class LocalWindows(views.APIView):
    def get(self, request):
        """
        Zainstalwoane lokalnie oprogramowania
        """
        windows_registry = WindowsRegistry()
        response = windows_registry.get_all_software()
        return Response(response)


class CommandsWindows(views.APIView):
    def get(self, request):
        hardware = Hardware()
        response = hardware.to_json()
        return Response(response)


class NetworkLocal(views.APIView):
    """Zwraca informacje o lokalnej sieci."""
    def get(self, request):
        return Response(LocalNetworkData().values)











@login_required
def login_required_view(request, cve_code):
    # cve = get_object_or_404() #jakby testowac z bazy
    cve = {"key": cve_code, "value": "test value"}
    return JsonResponse(cve)
