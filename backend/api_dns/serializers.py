from rest_framework import serializers


class ARecordDict(object):
    def __init__(self, dns):
        self.dns = dns

# create a serializer
class ARecordSerializer(serializers.Serializer):
    # intialize fields
    dns = serializers.DictField(
        child=serializers.CharField())