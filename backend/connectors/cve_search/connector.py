import requests
from requests.exceptions import HTTPError


from connectors.credential import Credential 
from connector_interface import ConnectorInterface


class Connector(ConnectorInterface):
    """
    http://cve-search.org/api/
    """
    def __init__(self, credentials):
        super().__init__(credentials)

    def search_by_cve_code(self, cve_code):
        url = f'{self.cve}{cve_code}'
        print(url)
        response = requests.get(url)
        return response

    def get_last_30_cves(self):
        response = requests.get(self.last)
        return response

    def get_vendors_list(self):
        response = requests.get(self.vendor)
        return response

    def get_vendor_products(self, vendor):
        url = f'{self.vendor}{vendor}/'
        response = requests.get(url)
        return response

    def get_product(self, vendor, product):
        url = f'{self.vendor}{vendor}/{product}'
        response = requests.get(url)
        return response

    def get_db_info(self):
        response = requests.get(self.db_info)
        return response



if __name__ == "__main__":
    # \sarenka\backend>python connectors\cve_search\connector.py  
    credentials = Credential().cve_search
    connector = Connector(credentials)
    print(connector.search_by_cve_code("CVE-2010-3333"))
    print(connector.get_last_30_cves())
    print(connector.get_vendors_list())
    print(connector.get_vendor_products("microsoft"))
    print(connector.get_product("microsoft","office"))
    print(connector.get_db_info())
