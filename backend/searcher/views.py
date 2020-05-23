import json
# import django_postgres_psycopg2
import psycopg2.extensions
# import django_postgres

from rest_framework import views
from rest_framework.response import Response
from rest_framework.generics import ListAPIView


from connectors.credential import Credential
from connectors.cve_search.connector import Connector
from .serializers import CveWrapperSerializer
from django.http import HttpResponse
from .models import Test

from django.shortcuts import get_object_or_404

from django.db import models


class Test_Class(views.APIView):
    
    def  ViewName(request, test_id):
        text2 = Test.objects.get(pk=test_id)
        return HttpResponse("%s" %text2)
    
class CVESearchView(views.APIView):

    def get(self, request, code):
        credentials = Credential().cve_search
        connector = Connector(credentials)
        cve = connector.search_by_cve_code(code)
        response = CveWrapperSerializer(instance=cve).data
        return Response(response)




