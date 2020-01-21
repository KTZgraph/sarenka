from typing import Dict, Tuple, Sequence
import json


class Credential:
    """Credentials for shodan, censys, etc"""

    def __init__(self, config_file="connectors/credentials.json")->None:
        with open(config_file) as f:
            self.__credentials = json.load(f)

    @property
    def shodan(self):
        return self.__credentials.get("shodan", {})

    @property
    def shodan_api_key(self):
        return self.shodan.get("api_key", {})

    @property
    def censys(self):
        return self.__credentials.get("censys", {})
