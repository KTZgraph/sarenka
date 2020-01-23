from typing import Dict, Tuple, Sequence
import json


class Credential:
    """Credentials for shodan, censys, etc"""
    __instance = None
    
    def __init__(self, config_file="connectors/credentials.json")->None:
        if not Credential.__instance:
            with open(config_file) as f:
                self.__credentials = json.load(f)
        else:
            self.getInstance()

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Credential()
        return cls.__instance

    @property
    def shodan(self):
        return self.__credentials.get("shodan", {})

    @property
    def shodan_api_key(self):
        return self.shodan.get("api_key", {})

    @property
    def censys(self):
        return self.__credentials.get("censys", {})
