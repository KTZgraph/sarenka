from rest_framework import serializers

from .models import CWEModel, TechnicalImpactModel


class SettingsSerializer(serializers.Serializer):
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


class CveWrapperSerializer(serializers.Serializer):
    cve = serializers.CharField()
    cvss_vector = serializers.CharField()
    complexity = serializers.CharField()
    authentication = serializers.CharField()
    vector = serializers.CharField()
    cvss = serializers.CharField()
    cwe = serializers.CharField()
    title = serializers.CharField()
    availability = serializers.CharField()
    confidentiality = serializers.CharField()
    products = ProductSerializer(many=True)


class CWEModelSerializer(serializers.HyperlinkedModelSerializer):
    """Serializowanie obiektu z bazy danych"""

    class Meta:
        model = CWEModel
        fields = ["cwe_id", "title", "description", "likehood"]

