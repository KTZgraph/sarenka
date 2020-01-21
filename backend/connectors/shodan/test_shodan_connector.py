import unittest

from connectors.credential import Credential 
from shodan_connector import ShodanConnector


class ShodanConnectorTest(unittest.TestCase):
    def setUp(self):
        self.api_key = Credential().shodan_api_key
        self.api_key_wrong = "wrong api key"

    # def test_create(self):
    #     self.assertIsNotNone(ShodanConnector(self.api_key))
    #     self.assertIsNotNone(ShodanConnector())
    #     self.assertIsNotNone(ShodanConnector(self.api_key_wrong))

    # def test_search(self):
    #     shodan_connector = ShodanConnector()
    #     shodan_connector.search("apache")

    def test_host(self):
        shodan_connector = ShodanConnector()
        shodan_connector.host("my_test_ip")

if __name__ == '__main__':
    unittest.main()