import unittest

from connectors.credential import Credential 
from connector import Connector


class ConnectorTest(unittest.TestCase):
    def setUp(self):
        self.shodan_credentials = Credential().shodan

    def test_create(self):
        self.assertIsNotNone(Connector(self.shodan_credentials))
        # self.assertIsNotNone(Connector())
        # self.assertIsNotNone(Connector(self.api_key_wrong))

    def test_search(self):
        connector = Connector(self.shodan_credentials)
        result = connector.search("apache")
        self.assertIsNotNone(result)
        for i in result:
            print(i)

    # def test_host(self):
    #     connector = Connector()
    #     connector.host("my_test_ip")

if __name__ == '__main__':
    unittest.main()

# cd sarenka\backend
# python connectors\shodan\test_connector.py  