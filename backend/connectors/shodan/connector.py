from typing import Dict, Tuple, Sequence, List, NoReturn
import shodan

from connectors.credential import Credential 
from connectors.shodan.connector_interface import ConnectorInterface
from connectors.shodan.host_wrapper import HostWrapper
from connectors.shodan.host_details_wrapper import HostDetailsWrapper

class Connector(ConnectorInterface):
    def __init__(self, shodan_credentials):
        super().__init__(shodan_credentials)
        self.api = shodan.Shodan(self.api_key)
    
    def search(self, query, amount=3)->[HostWrapper]:
        """Return list of hosts finded with software"""
        hosts = []
        try:
            results = self.api.search(query)
            for result in results['matches'][0:amount]:
                host = HostWrapper(result, query)
                hosts.append(host)
        
        except shodan.APIError as exception:
                print('Error: {}'.format(exception))
                # TODO: loggers
        finally:
            return hosts

    def host(self, ip, ports=[]):
        result = self.api.host(ip)
        host_details = HostDetailsWrapper(ip, result)
        return host_details
    
    def search_by_asn(self, asn):
        """
        https://www.shodan.io/search?query=asn%3AAS6846
        w censysie numer asn jest widoczny - punkt spięcia wyszukiwań
        z censysa "autonomous_system": {"description": "GOOGLE", "rir": "unknown", "routed_prefix": "8.8.8.0/24", "country_code": "US", "path": [15169], "asn": 15169, "name": "GOOGLE"}, 
        """
        pass