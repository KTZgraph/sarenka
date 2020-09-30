from django.test import RequestFactory
from django.urls import reverse, NoReverseMatch
import pytest
from django.test import TestCase

from api_dns.views import ARecordView


@pytest.mark.django_db
class TestARecordView(TestCase):

    @classmethod
    def setUpClass(cls):
        super(TestARecordView, cls).setUpClass()
        cls.factory = RequestFactory()

    def test_a_record(self):
        path = reverse('dns_record', kwargs={"fqdn": "examplefqd"})
        request = self.factory.get(path)
        response = ARecordView().get(request, fqdn="examplefqd")
        assert response.status_code == 200

    def test_a_record_no_fqdn(self):
        with self.assertRaises(NoReverseMatch):
            reverse('dns_record')
