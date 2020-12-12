from rest_framework import serializers


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


class ARecordDict(object):
    """Serializer dla danych DNS."""
    def __init__(self, dns):
        self.dns = dns


# create a serializer
class ARecordSerializer(serializers.Serializer):
    """Serializer dla danych DNS z A rekordu."""
    # intialize fields
    dns = serializers.DictField(
        child=serializers.CharField())