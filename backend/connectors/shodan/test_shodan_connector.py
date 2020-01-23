import unittest

from connectors.credential import Credential 
from connector import Connector


class ShodanConnectorTest(unittest.TestCase):
    def setUp(self):
        self.api_key = Credential().shodan_api_key
        self.api_key_wrong = "wrong api key"

    # def test_create(self):
    #     self.assertIsNotNone(Connector(self.api_key))
    #     self.assertIsNotNone(onnector())
    #     self.assertIsNotNone(Connector(self.api_key_wrong))

    # def test_search(self):
    #     connector = Connector()
    #     connector.search("apache")

    def test_host(self):
        connector = Connector()
        connector.host("my_test_ip")

if __name__ == '__main__':
    unittest.main()