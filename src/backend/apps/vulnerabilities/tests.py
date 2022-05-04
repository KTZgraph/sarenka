from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from apps.vulnerabilities import models


class CWETestCase(APITestCase):
    def test_create(self):
        data = {
            "code": "CWEDetails-123",
            "short_description": "short description",
            "description": "long description",
        }
        response = self.client.post(reverse("vulnerabilities:cwe-list"), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.post(reverse("vulnerabilities:cwe-list"), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class CVETestCase(APITestCase):
    def setUp(self) -> None:
        self.cwe = models.CWE.objects.create(
            code="CWEDetails-123",
            short_description="short description",
            description="long description",
        )

    def test_create(self):
        data = {
            "code": "CVE-1234-123",
            "description": "CVE description",
            "published": "1980-01-01",
            "updated": "2000-03-28",
            "cwe": 1,
        }
        response = self.client.post(reverse("vulnerabilities:cve-list"), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.post(reverse("vulnerabilities:cve-list"), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        data["cwe"] = 777777777
        response = self.client.post(reverse("vulnerabilities:cve-list"), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class VectorTestCase(APITestCase):
    def setUp(self) -> None:
        self.cwe = models.CWE.objects.create(
            code="CWEDetails-123",
            short_description="short description",
            description="long description",
        )

        self.cve = models.CVE.objects.create(
            code="CVE-1234-123",
            description="CVE description",
            published="1980-01-01",
            updated="2000-03-28",
            cwe=self.cwe,
        )

    def test_create_v3(self):
        data = {
            "version": "3",
            "code": "CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H",
            "base_score": "7.8",
            "base_severity": "2",
            "exploitability_score": "1.8",
            "impact_score": "5.9",
            "cve": 1,
        }

        response = self.client.post(reverse("vulnerabilities:vector-list"), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_v2(self):
        data = {
            "version": "2",
            "code": "AV:L/AC:L/Au:N/C:P/I:P/A:P",
            "base_score": "4.6",
            "base_severity": "1",
            "exploitability_score": "3.9",
            "impact_score": "6.4",
            "cve": 1,
        }

        response = self.client.post(reverse("vulnerabilities:vector-list"), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        data["cve"] = 999999
        response = self.client.post(reverse("vulnerabilities:vector-list"), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class ReferenceCase(APITestCase):
    def setUp(self) -> None:
        self.cwe = models.CWE.objects.create(
            code="CWEDetails-123",
            short_description="short description",
            description="long description",
        )

        self.cve = models.CVE.objects.create(
            code="CVE-1234-123",
            description="CVE description",
            published="1980-01-01",
            updated="2000-03-28",
            cwe=self.cwe,
        )

    def test_create(self):
        data = {
            "is_confirmed": True,
            "is_exploit": False,
            "is_vendor_advisory": True,
            "url": "https://www.intel.com",
            "cve": 1,
        }

        response = self.client.post(reverse("vulnerabilities:reference-list"), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        data["cve"] = 9999999999999999
        response = self.client.post(reverse("vulnerabilities:reference-list"), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class CPECase(APITestCase):
    def setUp(self) -> None:
        self.cwe = models.CWE.objects.create(
            code="CWEDetails-123",
            short_description="short description",
            description="long description",
        )

        self.cve = models.CVE.objects.create(
            code="CVE-1234-123",
            description="CVE description",
            published="1980-01-01",
            updated="2000-03-28",
            cwe=self.cwe,
        )

    def test_create(self):
        data = {
            "is_vulnerable": True,
            "version": "2.3",
            "code": "cpe:2.3:o::",
            "cve": 1,
        }

        response = self.client.post(reverse("vulnerabilities:cpe-list"), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        data["cve"] = 999999999999999
        response = self.client.post(reverse("vulnerabilities:cpe-list"), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
