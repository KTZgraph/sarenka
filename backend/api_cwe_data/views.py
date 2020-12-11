from rest_framework.views import APIView
from rest_framework.response import Response
from .mitre_scrapers import CWETableTop25Scraper, CWEDataScraper


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

