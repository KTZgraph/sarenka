from django.shortcuts import render

# Create your views here.
from rest_framework import generics, mixins
from rest_framework.response import Response

from .cwes.cwe_top_25 import CWETOP25


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