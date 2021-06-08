from rest_framework import viewsets
from rest_framework.generics import get_object_or_404

from .models import CensysCredentials, ShodanCredentials
from .serializers import CensysCredentialsSerializer, ShodanCredentialsSerializer


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
