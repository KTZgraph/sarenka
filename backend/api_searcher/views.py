from rest_framework import views
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
import logging, traceback

from connectors.credential import Credential
from connectors.cve_search.connector import Connector as CVEConnector
from connectors.censys.connector import Connector as CensysConnector
from .serializers import CveWrapperSerializer
from .scrapers import CWETableTop25Scraper, CWEDataScraper, NISTCVEScraper
from .a_record import ARecord, ARecordWrongFQDNError
from .serializers import ARecordDict, ARecordSerializer
from common.contact import Contact


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


class CensysHostSearchView(views.APIView):
    # TODO refaktor !
    """
    Wyszukiwanie danych po IP w censysie
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


class ARecordView(APIView):

    def get(self, request, fqdn='renmich.faculty.wmi.amu.edu.pl'):
        """
        Gets DNS A Record Data

        :param request: django request object
        :param fqdn: fully qualified domain name
        :return: dns data
        :example: fqdn='renmich.faculty.wmi.amu.edu.pl'
        """
        dns_func = {
            'ip': ARecord.get_ip,
            'cname': ARecord.get_cname,
            'mx': ARecord.get_mx,
            'ns': ARecord.get_ns,
            'dname': ARecord.get_dname,
            'aname': ARecord.get_aname
        }

        dns_data = {}
        for record_name in dns_func.keys():
            try:
                dns_data.update({record_name : dns_func.get(record_name)(fqdn)})
            except ARecordWrongFQDNError as err:
                dns_data.update({record_name: str(err)})
            except NotImplementedError:
                dns_data.update({record_name: Contact.get_contact(record_name.upper() + ' Record')})
            except KeyError:
                dns_data.update({"ARecord": f"record '{record_name}' is not supported"})

        obj = ARecordDict(dns_data)
        return Response(ARecordSerializer(obj).data)


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


class ARecordView(APIView):

    def get(self, request, fqdn='renmich.faculty.wmi.amu.edu.pl'):
        """
        Zwraca dane z rekordu A DNS

        :param request: django request object
        :param fqdn: fully qualified domain name
        :return: dns data
        :example: fqdn='renmich.faculty.wmi.amu.edu.pl'
        """
        dns_func = {
            'ip': ARecord.get_ip,
            'cname': ARecord.get_cname,
            'mx': ARecord.get_mx,
            'ns': ARecord.get_ns,
            'dname': ARecord.get_dname,
            'aname': ARecord.get_aname
        }

        dns_data = {}
        for record_name in dns_func.keys():
            try:
                dns_data.update({record_name : dns_func.get(record_name)(fqdn)})
            except ARecordWrongFQDNError as err:
                dns_data.update({record_name: str(err)})
            except NotImplementedError:
                dns_data.update({record_name: Contact.get_contact(record_name.upper() + ' Record')})
            except KeyError:
                dns_data.update({"ARecord": f"record '{record_name}' is not supported"})

        obj = ARecordDict(dns_data)
        return Response(ARecordSerializer(obj).data)


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


@login_required
def login_required_view(request, cve_code):
    # cve = get_object_or_404() #jakby testowac z bazy
    cve = {"key": cve_code, "value": "test value"}
    return JsonResponse(cve)