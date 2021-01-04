from rest_framework import views, status
from rest_framework.response import Response
from django.conf import settings
import json
import os

from api_searcher.third_services.service_details import ServiceDetails, ServiceDetailsError
from api_searcher.third_services.cve_circl.cve_circl_vendor_list import CveCirlVendorList


class VendorListView(views.APIView):
    """Widok Django zwracający dostawców oprogramowania z wykrytymi podatnościami CVE"""
    __feed_file_path = "feeds\\vendors\\vendors_all.json"

    def get_data(self):
        two_up = os.path.abspath(os.path.join(settings.BASE_DIR, "../.."))
        feed_path = os.path.join(two_up, self.__feed_file_path)
        with open(feed_path) as json_file:
            data = json.load(json_file)

        return data # zwraca w postaci jsona

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
            if not vendors:
                raise ServiceDetailsError("Unable to get data from https://cve.circl.lu/ service.")
            return Response({"vendor_list": vendors})

        except ServiceDetailsError as ex:
            return Response({"vendor_list":self.get_data(), "warning": "Data from feed files", "details": str(ex)})

        except Exception as ex:
            return Response({"error": "Unable to get vendor list. "
                                      "Please check information in file sarenka\\backend\\api_searcher\\third_services\\service_details.json",
                             "details": str(ex)}, status=status.HTTP_400_BAD_REQUEST)