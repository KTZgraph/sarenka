from rest_framework import serializers


class UserCredentialsSerializer(serializers.Serializer):
    """Serializuje klucze użytkownika do serwisów trzeich jak censys.io oraz shodan.io"""
    censys_API_ID = serializers.CharField(max_length=72)
    censys_Secret = serializers.CharField(max_length=64)
    shodan_user = serializers.CharField(max_length=200)
    shodan_api_key = serializers.CharField(max_length=64)

class ProductSerializer(serializers.Serializer):
    vendor = serializers.CharField()
    name = serializers.CharField()
    version = serializers.CharField()
    system = serializers.CharField()


