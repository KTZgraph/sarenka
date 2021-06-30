from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

import base64

from apps.vulnerabilities.api import serializers
from apps.vulnerabilities import models
from apps.vulnerabilities.cwes.cwe_top_25 import CWETOP25


class CWEList(generics.ListAPIView):
    serializer_class = serializers.CWESerializer
    queryset = models.CWE.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['code']  # Nie pozwala na tworzenie nowego CWE, dobre do predefiniowanych wartosci

    def get_queryset(self):
        cwe = self.request.query_params.get('cwe', None)


class CWEDetail(generics.RetrieveUpdateAPIView):
    serializer_class = serializers.CWESerializer
    queryset = models.CWE.objects.all()


class CVEList(generics.ListAPIView):
    serializer_class = serializers.CVESerializer
    queryset = models.CVE.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['cwe__code']  # by defautl exact match


class CWECVEList(generics.ListAPIView):
    """
    Filter by cwe code - return list of CVEs for specific CWE.
    """
    serializer_class = serializers.CVESerializer

    def get_queryset(self):
        cwe = self.kwargs['cwe']
        return models.CVE.objects.filter(cwe__code__icontains=cwe.upper())


class CVECreate(generics.CreateAPIView):
    serializer_class = serializers.CVESerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        cve = models.CVE.objects.filter(cwe__id=pk)
        return cve


class CVEDetail(generics.RetrieveUpdateAPIView):
    serializer_class = serializers.CVESerializer
    queryset = models.CVE.objects.all()


class VectorView(generics.ListCreateAPIView):
    serializer_class = serializers.VectorSerializer
    queryset = models.Vector.objects.all()


class VectorSeverityList(generics.ListAPIView):
    """
    Filter by severity level - return list of vectors by severity name from choice field (HIGH, MEDIUM, LOW).
    """
    serializer_class = serializers.VectorSerializer

    def get_queryset(self):
        severity = self.kwargs['severity']
        if severity.isdigit():
            severity_id = int(severity)
        else:
            severity_levels = {v: k for k, v in models.Vector.SEVERITY}
            severity_id = severity_levels[severity.upper()]
        return models.Vector.objects.filter(base_severity=severity_id)


class VectorSearch(generics.ListAPIView):
    """
    Filter by url parameters [cve, severity]
    """
    serializer_class = serializers.VectorSerializer

    def get_queryset(self):
        severity = self.request.query_params.get('severity', None)
        cve = self.request.query_params.get('cve', None)
        code_b64 = self.request.query_params.get('code', None)
        version = self.request.query_params.get('version', None)
        base_score = self.request.query_params.get('base_score', None)
        exp_score = self.request.query_params.get('exp_score', None)
        impact_score = self.request.query_params.get('impact_score', None)
        cwe = self.request.query_params.get('cwe', None)

        if severity is not None:
            if severity.isdigit():
                severity_id = int(severity)
            else:
                severity_levels = {v: k for k, v in models.Vector.SEVERITY}
                severity_id = severity_levels[severity.upper()]
            return models.Vector.objects.filter(base_severity=severity_id)

        if version is not None:
            try:
                version_id = float(version)
            except ValueError:
                version_list = {v: k for k, v in models.Vector.VERSION}
                version_id = version_list[version.upper()]
            return models.Vector.objects.filter(version=version_id)

        if cve is not None:
            cve = cve.upper()
            return models.Vector.objects.filter(cve__code=cve)

        if code_b64 is not None:
            code_base64_bytes = code_b64.encode("ascii")
            code_str_bytes = base64.b64decode(code_base64_bytes)
            code = code_str_bytes.decode('ascii')
            return models.Vector.objects.filter(code__icontains=code)

        if base_score is not None:
            return models.Vector.objects.filter(base_score=float(base_score))
        if exp_score is not None:
            return models.Vector.objects.filter(exploitability_score=float(exp_score))
        if impact_score is not None:
            return models.Vector.objects.filter(impact_score=float(impact_score))
        if cwe is not None:
            return models.Vector.objects.filter(cve__cwe__code__icontains=cwe)


class VectorDetail(generics.RetrieveUpdateAPIView):
    serializer_class = serializers.VectorSerializer
    queryset = models.Vector.objects.all()


class ReferenceList(generics.ListAPIView):
    serializer_class = serializers.ReferenceSerializer
    queryset = models.Reference.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['is_confirmed', 'is_exploit', 'is_vendor_advisory']
    # /api/vulns/reference-list/?is_confirmed=true; api/vulns/reference-list/?is_confirmed=true&is_exploit=true;
    # api/vulns/reference-list/?is_confirmed=true&is_exploit=true&is_vendor_advisory=true


class ReferenceCreate(generics.CreateAPIView):
    serializer_class = serializers.ReferenceSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        reference = models.Reference.objects.filter(cve__id=pk)
        return reference


class ReferenceDetail(generics.RetrieveUpdateAPIView):
    serializer_class = serializers.ReferenceSerializer
    queryset = models.Reference.objects.all()


class CPEList(generics.ListAPIView):
    serializer_class = serializers.CPESerializer
    queryset = models.CPE.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['is_vulnerable']  # api/vulns/cpe-list/?is_vulnerable=true


class CPECreate(generics.CreateAPIView):
    serializer_class = serializers.CPESerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        cpe = models.CPE.objects.filter(cve__id=pk)
        return cpe


class CPEDetail(generics.RetrieveUpdateAPIView):
    serializer_class = serializers.CPESerializer
    queryset = models.CPE.objects.all()
