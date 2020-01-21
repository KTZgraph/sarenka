from typing import Dict, Tuple, Sequence, List, NoReturn
import shodan

from connectors.credential import Credential 
from shodan_connector_interface import ShodanConnectorInterface
from shodan_host_wrapper import ShodanHostWrapper


class ShodanConnector(ShodanConnectorInterface):
    def __init__(self, api_key=""):
        super().__init__(api_key)
        if api_key:
            self.api_key = api_key
        else:
            self.api = shodan.Shodan(Credential().shodan_api_key)
    
    def search(self, query, amount=3):
        """Return list of hosts finded with software"""
        hosts = []
        try:
            results = self.api.search(query)
            for result in results['matches'][0:amount]:
                host = ShodanHostWrapper(result)
                hosts.append(host)
        
        except shodan.APIError as exception:
                print('Error: {}'.format(exception))
                # TODO: loggers
        finally:
            return hosts
