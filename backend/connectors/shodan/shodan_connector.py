import shodan


from shodan_connector_interface import ShodanConnectorInterface
from connectors.credential import Credential 

class ShodanConnector(ShodanConnectorInterface):
    def __init__(self, api_key=""):
        super().__init__(api_key)
        if api_key:
            self.api_key = api_key
        else:
            self.api = shodan.Shodan(Credential().shodan_api_key)
    
    def search(self, query):
        pass

