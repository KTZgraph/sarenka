import json
from rest_framework import views
from rest_framework.response import Response
from rest_framework.generics import ListAPIView

from connectors.credential import Credential
from connectors.cve_search.connector import Connector
from connectors.cve_search.connector import Connector
from .serializers import CveWrapperSerializer
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.db import models
from django.http import JsonResponse

    
class CVESearchView(views.APIView):

    def get(self, request, code):
        credentials = Credential().cve_search
        connector = Connector(credentials)
        cve = connector.search_by_cve_code(code)
        response = CveWrapperSerializer(instance=cve).data
        return Response(response)

class ListVendors(views.APIView):
    def get(self, request):
        credentials = Credential().cve_search
        connector = Connector(credentials)
        listVendors = connector.get_vendors_list()
        return Response(listVendors)