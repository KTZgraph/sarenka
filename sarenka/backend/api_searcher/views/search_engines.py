from rest_framework import views
from rest_framework.response import Response
from rest_framework import status
from rest_framework.reverse import reverse
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import logging

# refaktorowanie censysa
from api_searcher.search_engines.censys_engine.censys_host_search import CensysHostSearch, CensysHostSearchError
from api_searcher.searcher import Searcher
from api_searcher.views.common import Common
from api_searcher.search_engines.user_credentials import UserCredentials
logger = logging.getLogger('django')


class CensysHostSearchView(views.APIView):
    """
    Widok Django zwracający dane z wyszukiwartki http://censys.io/.
    Zwraca informacje o potenjcalne podatności hosta na ataki: "heartbleed", "logjam_attack", "freak_attack", "poodle_attack".
    """
    def get(self, request, ip_address):
        """Zwraca informacje uzyskane za pośrednictwem serwisu https://censys.io/.
        Na podstawie adresu ip hosta podane przez uzytkownika w żadaniu GET HTTP.
        :param request: obiekt request dla widoku Django
        :return: dane w postaci json zawierajace informacje o hoście zwrócone przez serwis https://censys.io/.
        """
        try:
            user_credentials = UserCredentials()
            response = CensysHostSearch(user_credentials).response(ip_address)
            return Response(response)
        except CensysHostSearchError as ex:
            host_address = Common(request).host_address
            settings_url = host_address + reverse('settings')
            return Response({"message": f"Please create account on https://censys.io/ and add valid credentials "
                                        f"for SARENKA app on {settings_url}",
                             "details": str(ex)}, status=status.HTTP_417_EXPECTATION_FAILED)


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
        user_credentials = UserCredentials()
        searcher = Searcher(host, user_credentials=user_credentials)
        return Response({"full_search": searcher.values})


@login_required
def login_required_view(request, cve_code):
    # cve = get_object_or_404() #jakby testowac z bazy
    cve = {"key": cve_code, "value": "test value"}
    return JsonResponse(cve)
