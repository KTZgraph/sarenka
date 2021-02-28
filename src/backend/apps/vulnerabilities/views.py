from django.shortcuts import render

# Create your views here.
from rest_framework import generics, mixins
from rest_framework.response import Response


class CVEGenericAPIView(generics.GenericAPIView,  mixins.ListModelMixin, mixins.RetrieveModelMixin):
    def get(self, request, pk=None):
        if pk:
            return Response({
                'data': "test response pk"
            })
        return Response({
            'data': "test response"
        })