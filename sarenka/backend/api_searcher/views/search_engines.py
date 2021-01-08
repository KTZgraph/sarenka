from rest_framework import views
from rest_framework.response import Response
from rest_framework import status
from rest_framework.reverse import reverse
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import logging

from api_searcher.search_engines.censys_engine.censys_host_search import CensysHostSearch, CensysHostSearchError
from api_searcher.search_engines.shodan_engine.shodan_host_search import ShodanHostSearch, ShodanHostSearchError
from api_searcher.searcher_full import SearcherFull
from api_searcher.views.common import Common
from api_searcher.search_engines.user_credentials import UserCredentials
logger = logging.getLogger('django')


class LocalUrlCreator:
    """Klasa pomocnicza generujaca urle do wnętrza aplikacji."""
    @staticmethod
    def get_user_credentials_url(request):
        return Common(request).host_address + reverse("user_credentials")





class CensysHostSearchView(views.APIView):
    """
    Widok Django zwracający dane z serwisu http://censys.io/.
    Zwraca informacje o potenjcalne podatności hosta na ataki: "heartbleed", "logjam_attack", "freak_attack", "poodle_attack".
    """
    def get(self, request, ip_address):
        """Zwraca informacje uzyskane za pośrednictwem serwisu https://censys.io/.
        Na podstawie adresu ip hosta podane przez uzytkownika w żadaniu GET HTTP.
        :param request: obiekt request dla widoku Django
        :return: dane w postaci json zawierajace informacje o hoście zwrócone przez serwis https://censys.io/.
        """
        settings_url = LocalUrlCreator.get_user_credentials_url(request)

        try:
            user_credentials = UserCredentials()
            response = CensysHostSearch(user_credentials).get_data(ip_address)
            return Response(response)
        except CensysHostSearchError as ex:
            return Response({"error": f"Please create account on https://censys.io/ service and add valid credentials "
                                        f"for SARENKA app on {settings_url}",
                             "details": str(ex)}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as ex:
            return Response({"error": f"Unable to get infromation from https://censys.io/ service.",
                             "details": str(ex)}, status=status.HTTP_400_BAD_REQUEST)


class ShodanHostSearchView(views.APIView):
    """
    Widok Django zwracający dane z serwisu https://shodan.io/.
    """
    def get(self, request, ip_address):
        """Zwraca informacje uzyskane za pośrednictwem serwisu https://censys.io/.
        Na podstawie adresu ip hosta podane przez uzytkownika w żadaniu GET HTTP.
        :param request: obiekt request dla widoku Django
        :return: dane w postaci json zawierajace informacje o hoście zwrócone przez serwis https://censys.io/.
        """
        settings_url = LocalUrlCreator.get_user_credentials_url(request)

        try:
            user_credentials = UserCredentials()
            response = ShodanHostSearch(user_credentials).get_data(ip_address)
            return Response({"shodan": response})
        except ShodanHostSearchError as ex:
            return Response({"error": f"Please create account on https://www.shodan.io/ service and add valid credentials "
                                        f"for SARENKA app on {settings_url}",
                             "details": str(ex)}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as ex:
            return Response({"error": f"Unable to get infromation from https://www.shodan.io/ service.",
                             "details": str(ex)}, status=status.HTTP_400_BAD_REQUEST)


class SearcherFullView(views.APIView):
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
        user_credentials = UserCredentials()
        searcher = SearcherFull(host, user_credentials=user_credentials)
        return Response({"full_search": searcher.values})


@login_required
def login_required_view(request, cve_code):
    # cve = get_object_or_404() #jakby testowac z bazy
    cve = {"key": cve_code, "value": "test value"}
    return JsonResponse(cve)
