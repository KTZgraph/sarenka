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
from .cve_and_cwe.mitre_cwe_scrapers import CWETableTop25Scraper, CWEDataScraper
from .cve_and_cwe.nist_cve_scrapers import  NISTCVEScraper
from .cve_and_cwe.cwe_all import CWEAll
from .cve_and_cwe.cve_details_all import CVEDetailsAll
from .cve_and_cwe.cwe_details_all import CWEDetailsAll


from .models import CWEModel, TechnicalImpactModel, CausedByModel, CVEModel
from .cwe_crud import CWECRUD
from .serializers import CWEModelSerializer

from .dns.dns_searcher import DNSSearcher, DNSSearcherFQDNError
from .windows.registry import WindowsRegistry
from .windows.hardware import Hardware
from .windows.network import LocalNetworkData
from .windows.local import LocalInfo
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
        try:
            server_address = self.get_server_address(request)
            nist_cve_scraper = NISTCVEScraper(code, server_address)
            return Response(nist_cve_scraper.get_data())
        except Exception:
            return Response({code: "Unable to get information - probably this CVE doesn't exists."})


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
        return Response(CWEDataScraper(id_cwe, server_address).get_data())


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
        return Response(CWEDataScraper(id_cwe, server_address).get_data())


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


class WindowsRegistryView(views.APIView):
    def get(self, request):
        """
        Zainstalwoane lokalnie oprogramowania
        """
        windows_registry = WindowsRegistry()
        response = windows_registry.get_all_software()
        return Response(response)


class WindowsHardwareView(views.APIView):
    def get(self, request):
        hardware = Hardware()
        response = hardware.to_json()
        return Response(response)


class NetworkLocalView(views.APIView):
    """Zwraca informacje o lokalnej sieci."""
    def get(self, request):
        return Response(LocalNetworkData().values)



class LocalView(views.APIView):
    """Zwraca informacje o lokalnej maszynie Windows"""
    def get(self, request):
        return Response(LocalInfo().values)


class CWEAllView(views.APIView):
    """Zwraca wszystkei kody CWE na podstawie pliku który został wygenerowany przez nas w innym narzędziu"""

    @staticmethod
    def get_server_address(request):
        """
        Zwraca adres do serwera aplikacji z uwzglednieniem protokołu np: http://127.0.0.1:8000/.
        Użycie - generpowanie urli do wewnątrz aplikacji.
        """
        host_address = request.get_host()
        # TODO: refaktor - milion kopii jes ttej funkcji
        if request.is_secure():
            address = "https://" + host_address
        else:
            address = "http://"+ host_address
        return address

    def get(self, request):
        server_address = self.get_server_address(request)
        response = CWEAll().render_output(server_address)
        return Response(response)


class CVEDetailsAllView(views.APIView):
    """Zwraca wszystkei kody CWE na podstawie pliku który został wygenerowany przez nas w innym narzędziu"""

    @staticmethod
    def get_server_address(request):
        """
        Zwraca adres do serwera aplikacji z uwzglednieniem protokołu np: http://127.0.0.1:8000/.
        Użycie - generpowanie urli do wewnątrz aplikacji.
        """
        host_address = request.get_host()
        # TODO: refaktor - milion kopii jes ttej funkcji
        if request.is_secure():
            address = "https://" + host_address
        else:
            address = "http://"+ host_address
        return address

    def get(self, request, page):
        server_address = self.get_server_address(request)
        response = CVEDetailsAll(page).render_output(server_address) #render_output(server_address)
        return Response(response)

################## CWE ##########################
class CWEDetailsAllView(views.APIView):
    """Zwraca wszystkei kody CWE z dokładdnymi informacjami
    - dlatego stronnicowanie / pojedyncze pliko po 100
    na podstawie pliku który został wygenerowany przez nas w innym narzędziu"""

    @staticmethod
    def get_server_address(request):
        """
        Zwraca adres do serwera aplikacji z uwzglednieniem protokołu np: http://127.0.0.1:8000/.
        Użycie - generpowanie urli do wewnątrz aplikacji.
        """
        host_address = request.get_host()
        # TODO: refaktor - milion kopii jes ttej funkcji
        if request.is_secure():
            address = "https://" + host_address
        else:
            address = "http://"+ host_address
        return address

    def get(self, request, page):
        server_address = self.get_server_address(request)
        # response = CWEDetailsAll(page).render_output(server_address) #render_output(server_address)
        response = CWEDetailsAll(page).get_data() #render_output(server_address)
        return Response(response)





######################################################
class AddCWEandCVE(views.APIView):

    def get(self, request):
        # nist_cve_scraper = NISTCVEScraper("CVE-2013-3621") CWE_NONE
        nist_cve_scraper = NISTCVEScraper("CVE-2019-4570")
        cve = nist_cve_scraper.get_data()

        cwe = cve["cwe"]

        # zapisz do bazy obiekt CWE
        cwe_crud = CWECRUD(cwe)
        cwe_crud.add()
        cwe_db_obj = cwe_crud.get()

        return Response({"message": "Żyjemy",
                         "cve": cve,
                         "cwe": cwe,
                         # "cwe_response": CWEModelSerializer(instance=cwe_db_obj).data,
                         "cwe_response": cwe_db_obj,
                         })





@login_required
def login_required_view(request, cve_code):
    # cve = get_object_or_404() #jakby testowac z bazy
    cve = {"key": cve_code, "value": "test value"}
    return JsonResponse(cve)
