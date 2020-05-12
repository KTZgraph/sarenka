from typing import Dict, Tuple, Sequence, List, NoReturn
import sys
import json
import requests
from censys.certificates import CensysCertificates
from censys.ipv4 import CensysIPv4
from censys.websites import CensysWebsites
from censys.base import CensysNotFoundException, CensysRateLimitExceededException, CensysUnauthorizedException

from connectors.credential import Credential 
from connector_interface import ConnectorInterface



class Connector(ConnectorInterface):
    def __init__(self, censys_credentials):
        super().__init__(censys_credentials)

    def search(self, query=''):
        res = requests.get(self.api_url + "/data", auth=(self.api_id, self.secret))
        if res.status_code != 200:
            print ("error occurred: %s" % res.json()["error"])
            sys.exit(1)
        print(type(res))
        return 0


    def host(self, ip):
        c = CensysIPv4(api_id=self.api_id, api_secret=self.secret)
        return c.view(ip)
        

if __name__ == "__main__":
    censys_credentials = Credential().censys
    connector = Connector(censys_credentials)
    print(connector.host("8.8.8.8"))