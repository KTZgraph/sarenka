from rest_framework import views, status
from rest_framework.response import Response

from api_searcher.third_services.service_details import ServiceDetails, ServiceDetailsError
from api_searcher.third_services.cve_circl.cve_circl_vendor_list import CveCirlVendorList


class VendorListView(views.APIView):
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
            credentials = ServiceDetails()
            connector = CveCirlVendorList(credentials)
            vendors = connector.get_data()
            return Response(vendors)
        except ServiceDetailsError:
            return Response({"error": "Unable to get vendor list.",
                             "details":  f"Please check information in file sarenka\\backend\\api_searcher\\third_services\\service_details.json"},
                                status=status.HTTP_401_UNAUTHORIZED)
        except Exception as ex:
            return Response({"error": "Unable to get vendor list.",
                             "details": str(ex)}, status=status.HTTP_400_BAD_REQUEST)