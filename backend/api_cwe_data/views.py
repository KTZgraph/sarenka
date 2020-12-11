from rest_framework.views import APIView
from rest_framework.response import Response
from .mitre_scrapers import CWETableTop25Scraper, CWEDataScraper


class CWETop25(APIView):
    def get(self, request):
        """
        Widok - zwraca informacje o TOP 25 najgroźniejszych słabościach oprogramowania
        """
        return Response({"response": CWETableTop25Scraper.get_top_25()})


class CWEData(APIView):
    """
    Zwraca infromacje o Common Weakness Enumeration na podstawie podane numeru CWE ID.
    http://127.0.0.1:8000/cwe/79
    http://127.0.0.1:8000/cwe/CWE-79
    http://127.0.0.1:8000/cwe/cwe-79

    """
    def get(self, request, id_cwe):
        return Response(CWEDataScraper(id_cwe).get_data())

