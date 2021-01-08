from rest_framework import serializers
from django.shortcuts import get_object_or_404
from .models import CensysCredentialsModel, ShodanCredentialsModel


class CensysCredentailsSerializer(serializers.ModelSerializer):
    """Serializer dla danych uwierzytelniajacych użytkownika do serwisu https://censys.io/"""
    class Meta:
        model = CensysCredentialsModel
        fields = ["api_id", "secret"]



class ShodanCredentailsSerializer(serializers.ModelSerializer):
    """Serializer dla danych uwierzytelniajacych użytkownika do serwisu https://www.shodan.io/"""
    class Meta:
        model = ShodanCredentialsModel
        fields = ["user", "api_key"]


class UserCredentialsSerializer(serializers.Serializer):
    """Serializuje klucze użytkownika do serwisów trzeich jak censys.io oraz shodan.io"""
    censys = CensysCredentailsSerializer(read_only=False, many=False)
    shodan = ShodanCredentailsSerializer(read_only=False, many=False)



class ProductSerializer(serializers.Serializer):
    vendor = serializers.CharField()
    name = serializers.CharField()
    version = serializers.CharField()
    system = serializers.CharField()


