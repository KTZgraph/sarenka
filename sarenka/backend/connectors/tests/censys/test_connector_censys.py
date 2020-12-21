import unittest

from connectors.credential import Credential 
from connectors.censys.connector import Connector


class TestConnectorCensys(unittest.TestCase):
    """
    cd sarenka\backend
    py.test
    """
    def setUp(self):
        self.censys_credentials = Credential().censys

    def test_create(self):
        self.assertIsNotNone(Connector(self.censys_credentials))
        # self.assertIsNotNone(Connector())
        # self.assertIsNotNone(Connector(self.api_key_wrong))

    def test_search_by_ip(self):
        connector = Connector(self.censys_credentials)
        result = connector.search_by_ip("8.8.8.8")
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()

