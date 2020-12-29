from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api_searcher.dns.dns_searcher import DNSSearcher, DNSSearcherError


class DNSSearcherView(APIView):
    """Widok Django który zwraca informacje o rekordach DNS dla dane hosta."""

    def get(self, request, host):
        """
        Metoda zwracajace informacje o rekordach DNS na podstawie zapytania GET HTTP użytkownika.
        :param request: obiekt dla widoku Django z informacjami od użytkownika
        :param host: fully qualified domain name
        :return: dns data
        :example: host='renmich.faculty.wmi.amu.edu.pl'
        """
        try:
            data = DNSSearcher(host).get_data()
            return Response({"dns_data" : data})
        except DNSSearcherError as ex:
            return Response({"error": f"Host doesn't exists", "details": str(ex)},
                     status=status.HTTP_400_BAD_REQUEST)
        except BaseException as ex:
            return Response({"error": f"Unable to get DNS record data for host={host}.", "details": str(ex)},
                     status=status.HTTP_404_NOT_FOUND)