import unittest
import os
from pathlib import Path

from connectors.shodan.connector import Connector
from connectors.credential import Credential 
from connectors.shodan.host_wrapper import HostWrapper
from connectors.shodan.web_app_searching import WebAppSearching


class WebAppSearchingTest(unittest.TestCase):
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
        self.connector = Connector(self.shodan_credentials)                
        host_data = {"ip_str": "my_test_ip"}
        host = HostWrapper(host_data, "my_software_name")

    def test_create(self):
        host = HostWrapper({"ip_str": "my_test_ip"}, "my_software_name")
        web_app_searching = WebAppSearching(host)
        print(web_app_searching)
        self.assertIsNotNone(9)

    def test_search(self):
        #TODO: zamockować API
        connector = Connector(self.shodan_credentials)
        connector.search("apache")


if __name__ == '__main__':
    unittest.main()
