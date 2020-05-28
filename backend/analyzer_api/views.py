import json
from django.shortcuts import render
from rest_framework import views
from rest_framework.response import Response
from rest_framework.generics import ListAPIView

from analyzer.analyzer_facade import AnalyzerFacade
from analyzer.softwares.imagemagick import ImageMagick
from connectors.credential import Credential
from connectors.cve_search.connector import Connector
from .serializers import ImageMagickSerializer

from local_installed.windows.registry import WindowsRegistry

class ImageMagickFileView(views.APIView):

    def get(self, request):
        file_with_cves = "C:\\Users\\dp\\Desktop\\sarenka\\backend\\analyzer\\imagemagic_cve.txt"
        image_magick = ImageMagick()
        analyzer_facade = AnalyzerFacade(image_magick)
        sorted_by_version = analyzer_facade.version_data_from_file(filename=file_with_cves)
        return Response(sorted_by_version)


class ImageMagickListView(views.APIView):

    def get(self, request):
        cve_list = ["CVE-2019-10131", "CVE-2019-11470"]
        image_magick = ImageMagick()
        analyzer_facade = AnalyzerFacade(image_magick)
        sorted_by_version = analyzer_facade.version_data_from_list(cve_list)
        return Response(sorted_by_version)


class ImageMagickUrlView(views.APIView):
    """
    Dane z urla np https://www.cvedetails.com/vulnerability-list/vendor_id-1749/product_id-3034/Imagemagick-Imagemagick.html
    tylko brak api - beautiful soup do parsowania danych z htmla
    """
    def get(self, request):
        response = {"TODO: ": "z urla"}
        return Response(response)


class LocalWindows(views.APIView):
    def get(self, request):
        """
        Zainstalwoane lokalnie oprogramowania
        """
        windows_registry = WindowsRegistry()
        response = windows_registry.get_all_software()
        return Response(response)
