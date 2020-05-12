from django.shortcuts import render
import json
from rest_framework import views
from rest_framework.response import Response
from rest_framework.generics import ListAPIView


from analyzer.imagemagick import ImageMagickFacade
from connectors.credential import Credential
from connectors.cve_search.connector import Connector
from .serializers import ImageMagickSerializer



class ImageMagickFileView(views.APIView):

    def get(self, request):
        file_with_cves = "imagemagic_cve.txt"
        sorted_by_version = ImageMagickFacade.version_data_from_file(filename=file_with_cves, files_save=False)
        return Response(sorted_by_version)

class ImageMagickListView(views.APIView):

    def get(self, request):
        cve_list = ["CVE-2019-10131", "CVE-2019-11470"]
        sorted_by_version = ImageMagickFacade.version_data_from_list(cve_list)
        return Response(sorted_by_version)

class ImageMagickUrlView(views.APIView):

    def get(self, request):
        response = {"TODO: ": "z urla"}
        return Response(response)