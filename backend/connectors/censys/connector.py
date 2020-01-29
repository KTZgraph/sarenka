from typing import Dict, Tuple, Sequence, List, NoReturn
import sys
import json
import requests

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


    def host(self, ip, ports=[]):
        pass
        