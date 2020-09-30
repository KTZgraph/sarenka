from django.urls import reverse, resolve


class TestSearcherUrls:
    def test_cve_url(self):
        path = reverse('get_by_cve', kwargs={"code": "CVE-2010-3333"})
        assert resolve(path).view_name == "get_by_cve"