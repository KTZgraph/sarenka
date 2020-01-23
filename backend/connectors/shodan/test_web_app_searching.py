import unittest

from connector import Connector
from host_wrapper import HostWrapper
from web_app_searching import WebAppSearching


class WebAppSearchingTest(unittest.TestCase):
    def setUp(self):
        self.connector = Connector()                
        host_data = {"ip_str": "my_test_ip"}
        self.host = HostWrapper(host_data, "my_software_name")

    def test_create(self):
        self.assertIsNotNone(WebAppSearching(self.host))

    def test_search(self):
        connector = Connector()
        connector.search("apache")


if __name__ == '__main__':
    unittest.main()