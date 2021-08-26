from rest_framework import serializers

from apps.vulnerabilities import models


class CPESerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CPE
        fields = '__all__'


class ReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Reference
        fields = '__all__'


class VectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vector
        fields = '__all__'


class CVESerializer(serializers.ModelSerializer):
    vector_list = VectorSerializer(many=True, read_only=True)
    reference_list = ReferenceSerializer(many=True, read_only=True)
    cpe_list = CPESerializer(many=True, read_only=True)

    class Meta:
        model = models.CVE
        fields = '__all__'


class CWESerializer(serializers.ModelSerializer):
    # cve_list = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = models.CWE
        fields = '__all__'
