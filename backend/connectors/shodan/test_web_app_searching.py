import unittest

from shodan_connector import ShodanConnector
from shodan_host_wrapper import ShodanHostWrapper
from web_app_searching import WebAppSearching


class WebAppSearchingTest(unittest.TestCase):
    def setUp(self):
        self.shodan_connector = ShodanConnector()                
        host_data = {"ip_str": "my_test_ip"}
        self.host = ShodanHostWrapper(host_data, "my_software_name")

    def test_create(self):
        self.assertIsNotNone(WebAppSearching(self.host))

    def test_search(self):
        shodan_connector = ShodanConnector()
        shodan_connector.search("apache")


if __name__ == '__main__':
    unittest.main()