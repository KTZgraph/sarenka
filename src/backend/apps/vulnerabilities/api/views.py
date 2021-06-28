from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from rest_framework import generics, viewsets

from rest_framework import generics, mixins
from rest_framework.response import Response

from apps.vulnerabilities.api import serializers
from apps.vulnerabilities import models
from apps.vulnerabilities.cwes.cwe_top_25 import CWETOP25


class CWEView(generics.ListCreateAPIView):
    serializer_class = serializers.CWESerializer
    queryset = models.CWE.objects.all()



class CVEGenericAPIView(generics.GenericAPIView,  mixins.ListModelMixin, mixins.RetrieveModelMixin):
    def get(self, request, pk=None):
        if pk:
            return Response({
                'data': "CVE test response pk"
            })
        return Response({
            'data': "CVE test response"
        })


class CWEGenericAPIView(generics.GenericAPIView,  mixins.ListModelMixin, mixins.RetrieveModelMixin):
    def get(self, request, pk=None):
        if pk:
            return Response({
                'data': "CWE test response pk"
            })

        return Response({
            'data': CWETOP25().get()
        })