import json
from rest_framework import views
from rest_framework.response import Response
from rest_framework.generics import ListAPIView

from connectors.credential import Credential
from connectors.cve_search.connector import Connector as CVEConnector
from connectors.censys.connector import Connector as CensysConnector
from .serializers import CveWrapperSerializer
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.db import models
from django.http import JsonResponse


class CVESearchView(views.APIView):

    def get(self, request, code):
        credentials = Credential().cve_search
        connector = CVEConnector(credentials)
        cve = connector.search_by_cve_code(code)
        response = CveWrapperSerializer(instance=cve).data
        return Response(response)


class CensysHostSearchView(views.APIView):
    # TODO refaktor !
    """
    Wyszukiwanie danych po IP w censysie
    opakowane protokoyły:
        - DNS
        - HTTPS
        - TLS
        - ataki "heartbleed", "logjam_attack", "freak_attack", "poodle_attack"
    """
    def get(self, request, ip_address):
        credentials = Credential().censys
        connector = CensysConnector(credentials)
        response = connector.search_by_ip(ip_address) # 
        return Response(response.to_json)


class ListVendors(views.APIView):
    def get(self, request):
        credentials = Credential().cve_search
        connector = Connector(credentials)
        listVendors = connector.get_vendors_list()
        return Response(listVendors)
