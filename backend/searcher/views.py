import json
from rest_framework import views
from rest_framework.response import Response
from rest_framework.generics import ListAPIView


from connectors.credential import Credential
from connectors.cve_search.connector import Connector
from .serializers import CveWrapperSerializer

class CVESearchView(views.APIView):

    def get(self, request, code):
        credentials = Credential().cve_search
        connector = Connector(credentials)
        cve = connector.search_by_cve_code(code)
        response = CveWrapperSerializer(instance=cve).data
        return Response(response)