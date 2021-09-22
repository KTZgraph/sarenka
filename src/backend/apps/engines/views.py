from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import CensysCredentials, ShodanCredentials
from .serializers import CensysCredentialsSerializer, ShodanCredentialsSerializer
# from .shodan_queries import shodan_queries
from .shodan_queries import ShodanQueries


class CensysCredentialsView(viewsets.ModelViewSet):
    serializer_class = CensysCredentialsSerializer

    def get_object(self, queryset=None, **kwargs):
        return get_object_or_404(CensysCredentials, pk=1)

    # Define Custom Queryset
    def get_queryset(self):
        return CensysCredentials.credentials


class ShodanCredentialsView(viewsets.ModelViewSet):
    serializer_class = ShodanCredentialsSerializer

    def get_object(self, queryset=None, **kwargs):
        return get_object_or_404(ShodanCredentials, pk=1)

    # Define Custom Queryset
    def get_queryset(self):
        return ShodanCredentials.credentials


@api_view(['GET'])
def get_shodan_queries(request):
    http_component = ShodanQueries().get_http_component()
    return Response({"result": http_component})
