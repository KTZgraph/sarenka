from rest_framework import views
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.reverse import reverse
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import logging

from connectors.credential import Credential, CredentialsNotFoundError
from connectors.cve_search.connector import Connector as CVEConnector

# refaktorowanie censysa
from .censys_data import censys_host_search


from .cve_and_cwe.mitre_cwe_scrapers import CWETableTop25Scraper, CWEDataScraper
from .cve_and_cwe.nist_cve_scrapers import  NISTCVEScraper
from .cve_and_cwe.cwe_all import CWEAll
from .cve_and_cwe.cve_details_all import CVEDetailsAll
from .cve_and_cwe.cwe_details_all import CWEDetailsAll

from .cwe_crud import CWECRUD

from .searcher import Searcher
from .views_common import Common

logger = logging.getLogger('django')


class CensysHostSearchView(views.APIView):
    """
    Wyszukiwanie danych po IP
    opakowane protokoyły:
        - DNS
        - HTTPS
        - TLS
        - ataki "heartbleed", "logjam_attack", "freak_attack", "poodle_attack"
    """
    def get(self, request, ip_address):
        """Zwraca informacje uzyskane za pośrednictwem serwisu https://censys.io/."""
        try:
            response = censys_host_search.CensysHostSearch.response(ip_address)
            return Response(response)
        except censys_host_search.CensysHostSearchError as ex:
            host_address = Common(request).host_address
            settings_url = host_address + reverse('settings')
            return Response({"message": "Please create account on https://censys.io/ and add valid credentials "
                                        "to SARENKA's settings",
                             "details": str(ex),
                             "url": settings_url})


class CVESearchView(views.APIView):
    def get(self, request, code):
        """
        Zwraca infromacje o konkrentje podatności po id CVE

        """
        print("CVESearchView")
        logger.debug("Logger at CVESearchView test message")
        logger.warning("Logger at CVESearchView test message")
        logger.info("Logger at CVESearchView test message")
        logger.error("Logger at CVESearchView test message")
        try:
            server_address = Common(request).host_address
            nist_cve_scraper = NISTCVEScraper(code, server_address)
            return Response(nist_cve_scraper.get_data())
        except Exception as ex:
            return Response({code: "Unable to get information - probably this CVE doesn't exists.", "details": str(ex)},
                            status=status.HTTP_400_BAD_REQUEST)


class CWETop25(APIView):
    """Widok Django zwracający informacje o TOP 25 najgroźniejszych słabościach oprogramowania."""
    def get(self, request):
        """
        Metoda zwracająca dane o 25 najpopularniejszych słabościach oprogramowania na podstawie żądania GET HTTP.
        Dane pochodzą ze strony https://cwe.mitre.org/top25/archive/2020/2020_cwe_top25.html
        :tags: CWE
        :param request: obiekt request dla widoku Django
        :return: dane w postaci json zawierajace ingormacje o hoście
        """
        try:
            server_address = Common(request).host_address
            return Response({"response": CWETableTop25Scraper(server_address).get_top_25()})
        except Exception as ex:
            return Response({"error": "Unable to get TOP 25 CWE from https://cwe.mitre.org/top25/archive/2020/2020_cwe_top25.html",
                             "details": str(ex)}, status=status.HTTP_404_NOT_FOUND)


class CWEData(APIView):
    """
    Widok Django zwracajacy infromacje o Common Weakness Enumeration na podstawie podanego numeru CWE ID.
    :tags: CWE
    """
    def get(self, request, id_cwe:str):
        """
        Metoda zwracająca dane o słabości oprogramowania na podstawie identyfikatora CWE podanego przez użytkownika
        w zapytaniu GET HTTP.
        :tags: CWE
        :param request: obiekt request dla widoku Django
        :param id_cwe: kod identyfikujący słabość oprogramowania
        :return: json z danymi wybranej słabości oprogramowania
        """
        try:
            server_address = Common(request).host_address
            return Response(CWEDataScraper(id_cwe, server_address).get_data())
        except AttributeError:
            return Response({"message": f"Unable to get information about CWE={id_cwe}.",
                             "details": f" Please check if CWE with id={id_cwe} exists on https://cwe.mitre.org/."},
                            status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            return Response({"error": f"Unable to get data.",
                             "details": str(ex)},
                            status=status.HTTP_404_NOT_FOUND)

class SearcherView(views.APIView):
    """
    Widok Django zwracajacy wszystkie dane dla hostu podanego przez użytkownika.
    Zawiera dane ze wszsytkich serwisów trzecich, informacje o DNS oraz banner.
    """
    def get(self, request, host):
        """
        Metoda zwracajace wszystkie dane o podanym przez użytkownika hoście na zapytanie GET HTTP.
        :param request: obiekt dla widoku Django z informacjami od użytkownika
        :param host: string mający adres ip lub domenę np.: python.org
        :return: dane w postaci json zawierajace ingormacje o hoście
        """
        ip_address = Common.get_ip_addres(host=host)
        searcher = Searcher(ip_address)
        return Response(searcher.values)


class ListVendors(views.APIView):
    """Widok Django zwracający dostawców oprogramowania z wykrytymi podatnościami CVE"""

    def get(self, request):
        """
        Metoda zwracajace dostawców dla których wykryto podatności Common Vulnerabilities and Exposures (CVE)
        na podstawie zapytania GET HTTP użytkownika. Wymaga uzupełnionych danych la serwisów trzecich.
        :tags: CVE
        :param request: obiekt dla widoku Django z informacjami od użytkownika
        :return: dane w postaci json zawierajace ingormacje o dostawcach dla których istnieją podntości CVE
        """
        try:
            credentials = Credential().cve_search
            connector = CVEConnector(credentials)
            vendors = connector.get_vendors_list()
            return Response(vendors)
        except CredentialsNotFoundError:
            host_address = Common(request).host_address
            settings_url = host_address + reverse('settings')
            return Response({"error": "Unable to get vendor list.",
                             "details":  f"Please check settings on {settings_url}"},
                                status=status.HTTP_400_BAD_REQUEST)
        except BaseException as ex:
            return Response({"error": "Unable to get vendor list.",
                             "details": str(ex)}, status=status.HTTP_400_BAD_REQUEST)


class CWEAllView(views.APIView):
    """Widok Django zwracający wszystkie kody CWE z podstawowywmi danymi takimi jak datę pobrania danych, źródło danych,
    identyfikator slabości, opis słabości, url do serwisu https://cwe.mitre.org ze szczegółowymi danymi,
    url do aplikacji SARENKA z najważniejszymi informacjami o konkretnej słabości."""

    def get(self, request):
        """
        Metoda zwracajaca podstawowe dane o wszystkich słabościach CWE z oficjalnego serwisu https://cwe.mitre.org.
        :param request: obiekt dla widoku Django z informacjami od użytkownika
        :return: podstawowe dane w formacie json o wszystkich słabościach CWE zawartych w feedach
        """
        try:
            server_address = Common(request).host_address
            response = CWEAll().render_output(server_address)
            return Response(response)
        except Exception as ex:
            Response({"error": "Unable to get all Common Weakness Enumeration data. "
                               "Please check is file sarenka/feedes/cwe_ids/cwe_all.json exists",
                      "details": str(ex)}, status=status.HTTP_404_NOT_FOUND)


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
        response = CWEDetailsAll(page).render_output(server_address) #render_output(server_address)
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
