import unittest
from unittest.mock import patch
import requests
import os
from pathlib import Path

from connectors.cve_search import connector
from connectors.credential import Credential 

def mocked_requests_get(*args, **kwargs):
    """
    Mockowanie zwrotki odpowiedzi get z zewnętrznego serwisu
    """
    class MockResponse:
        def __init__(self, json_data, status_code, ok):
            self.json_data = json_data
            self.status_code = status_code
            self.ok = ok

        def json(self):
            return self.json_data

    if args[0] == 'http://cve-search.org/api/existing_cve_code_1':
        return MockResponse({"key1": "value1"}, 200, True)
    elif args[0] == 'http://cve-search.org/api/existing_cve_code_2':
        return MockResponse({"key2": "value2"}, 200, True)

    return MockResponse(None, 404, False)


class TestConnectorCVESearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        Ścieżka do pliku z credentialami użytkownika do serwisów trzecich
        """
        dir_path = os.path.dirname(os.path.realpath(__file__))
        path = Path(dir_path)
        connectors_path = path.parent.parent
        cls.credentials_file_path = os.path.join(connectors_path, "credentials.example.json")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    def setUp(self):
        self.connector = connector.Connector(Credential(self.credentials_file_path).cve_search)
        self.existing_cve_code = "CVE-2019-1010298"
        self.not_existing_cve_code = "CVE-2012-0000000"

    def test_connect_status(self):
        with patch('connectors.cve_search.connector.requests.get') as mocked_get:
            mocked_get.return_value.ok = True 
            mocked_get.return_value.text ="Success" 
            response = self.connector.connect(self.existing_cve_code)
            mocked_get.assert_called_with("CVE-2019-1010298")

            mocked_get.return_value.ok = False 
            with self.assertRaises(connector.CVESearchConnectioError):
                response = self.connector.connect(self.existing_cve_code)
                mocked_get.assert_called_with("CVE-2019-1010298")

    @patch('connectors.cve_search.connector.requests.get', side_effect=mocked_requests_get)
    def test_connect_response(self, mock_get):
        response = self.connector.connect("http://cve-search.org/api/existing_cve_code_1")
        self.assertEqual(response, {"key1": "value1"})

        response = self.connector.connect("http://cve-search.org/api/existing_cve_code_2")
        self.assertEqual(response, {"key2": "value2"})

        with self.assertRaises(connector.CVESearchConnectioError):
            response = self.connector.connect('http://nonexistenturl.com/cantfindme.json')


if __name__ == "__main__":
    unittest.main()