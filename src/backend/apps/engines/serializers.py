from rest_framework import serializers

from .models import CensysCredentials,  ShodanCredentials


class ShodanCredentialsSerializer(serializers.ModelSerializer):
    base_url = serializers.ReadOnlyField()
    api_url = serializers.ReadOnlyField()

    class Meta:
        model = ShodanCredentials
        fields = ('user', 'api_key', 'base_url', 'api_url')


class CensysCredentialsSerializer(serializers.ModelSerializer):
    base_url = serializers.ReadOnlyField()
    api_url = serializers.ReadOnlyField()

    class Meta:
        model = CensysCredentials
        fields = ('api_id', 'secret', 'base_url', 'api_url')
