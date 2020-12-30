import unittest
import os
from pathlib import Path

from connectors.credential import Credential 
from connectors.shodan.connector import Connector


class TestConnectorShodan(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        """
        Ścieżka do pliku z credentialami użytkownika do serwisów trzecich
        """
        dir_path = os.path.dirname(os.path.realpath(__file__))
        path = Path(dir_path)
        connectors_path = path.parent.parent
        cls.credentials_file_path = os.path.join(connectors_path, "settings.example.json")

    def setUp(self):
        self.shodan_credentials = Credential(self.credentials_file_path).shodan

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