from django.urls import reverse, resolve


class TestApiDNSUrls:
    def test_a_record_url(self):
        path = reverse('dns_record', kwargs={"fqdn": "test_fqdn"})
        assert resolve(path).view_name == "dns_record"