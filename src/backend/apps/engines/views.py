from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import mixins, generics, status
from rest_framework.reverse import reverse

from .models import CensysCredentials, ShodanCredentials
from .serializers import CensysCredentialsSerializer, ShodanCredentialsSerializer


class CredentialsAPI(generics.GenericAPIView, mixins.RetrieveModelMixin):
    def get(self, request):

        shodan = ShodanCredentials.object()
        censys = CensysCredentials.object()


        return Response({
            'shodan': str(shodan),
            'censys': str(censys)
        })