from rest_framework import serializers

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
    # products = to_dict() for p in self.products]