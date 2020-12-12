from typing import Dict, Tuple, Sequence, List, NoReturn
import sys
import json
import mmh3
import requests
import codecs
from censys.certificates import CensysCertificates
from censys.ipv4 import CensysIPv4
from censys.websites import CensysWebsites
from censys.base import CensysNotFoundException, CensysRateLimitExceededException, CensysUnauthorizedException

from connectors.credential import Credential 
from connectors.censys.connector_interface import ConnectorInterface
from common.common import Common
from connectors.censys.wrappers.ip_wrapper import IPWrapper


class Connector(ConnectorInterface):
    def __init__(self, censys_credentials):
        super().__init__(censys_credentials)

    def search_by_ip(self, ip):
        """
        https://censys.io/ipv4/8.8.8.8
        """
        response = self.ipv4.view(ip)
        return IPWrapper(response)
        # Common.save_dict_to_file("50_56_73_47.json", response)
        # return response

    def search_by_fingerprint(self, certificate_hash):
        return self.certificate.view(certificate_hash)

    def search_by_website(self, domain):
        return self.website.view(domain)

    def search_favicon_murmur3(self, ip): #TODO spiąc z głównym jsonem odpowiedzi
        """ Wartośc niekryptogrficznego hasha dla faviconki strony"""
        favicon_hash = None
        try:
            response = requests.get('https://cybersecurity.wtf/favicon.ico')
            favicon = codecs.encode(response.content, "base64")
            favicon_hash = mmh3.hash(favicon)
        except BaseException as ex:
            # nie każda strona webowa ma favikonki
            pass

        return {"favicon_hash": favicon_hash}

if __name__ == "__main__":
    censys_credentials = Credential().censys
    connector = Connector(censys_credentials)
    response = connector.search_by_ip("8.8.8.8") # 
    # response = connector.search_by_ip("212.77.98.9") # dziala
    # response = connector.search_by_ip("50.56.73.47") # dziala
    Common.save_dict_to_file("8_8_8_8.json", response.to_json)

    # print(response)
    # Common.save_dict_to_file("C:\\Users\\dp\\Desktop\\sarenka\\backend\\connectors\\censys\\censys_ip.json", response)
    # print(connector.search_by_fingerprint("48177e03b47bdcb3b6ab28a92f8005b95302418cd5b9ede77a97eb918e4a2da2"))
    # print(connector.search_by_fingerprint("48177e03b47bdcb3b6ab28a92f8005b95302418cd5b9ede77a97eb918e4a2da2"))