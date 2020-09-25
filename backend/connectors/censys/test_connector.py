import unittest

from connectors.credential import Credential 
from connector import Connector


class TestConnector(unittest.TestCase):
    def setUp(self):
        self.censys_credentials = Credential().censys

    def test_create(self):
        self.assertIsNotNone(Connector(self.censys_credentials))
        # self.assertIsNotNone(Connector())
        # self.assertIsNotNone(Connector(self.api_key_wrong))

    def test_search(self):
        connector = Connector(self.censys_credentials)
        result = connector.search("22-ssh-banner-full_ipv4")
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()

# cd sarenka\backend
# python connectors\censys\test_connector.py  