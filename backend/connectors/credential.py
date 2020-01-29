from typing import Dict, Tuple, Sequence
import json

class CredentialData:
    def __init__(self, data):
        self.__base_url = data["base_url"]
        self.__api_key = data.get("api_key")
        self.__user = data.get("user")

    @property
    def base_url(self):
        return self.__base_url
    
    @property
    def api_key(self):
        return self.__api_key
    
    @property
    def user(self):
        return self.__user


class Credential:
    """Credentials for shodan, censys, etc"""
    __instance = None
    
    def __init__(self, config_file="connectors/credentials.json")->None:
        if not Credential.__instance:
            with open(config_file) as f:
                data = json.load(f)
            
            self.__binaryedge = CredentialData(data["binaryedge"])
            self.__censys = CredentialData(data["censys"])
            self.__fofa = CredentialData(data["fofa"])
            self.__publicwww = CredentialData(data["publicwww"])
            self.__urlscan = CredentialData(data["urlscan"])
            self.__whois = CredentialData(data["whois"])
            self.__shodan = CredentialData(data["shodan"])
            self.__yandex = CredentialData(data["yandex"])
            self.__zoomeye = CredentialData(data["zoomeye"])
        else:
            self.getInstance()

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Credential()
        return cls.__instance

    @property
    def binaryedge(self):
        return self.__binaryedge
    
    @property
    def censys(self):
        return self.__censys
    
    @property
    def fofa(self):
        return self.__fofa

    @property
    def publicwww(self):
        return self.__publicwww
    
    @property
    def urlscan(self):
        return self.__urlscan

    @property
    def whois(self):
        return self.__whois

    @property
    def shodan(self):
        return self.__shodan

    @property
    def yandex(self):
        return self.__yandex

    @property
    def zoomeye(self):
        return self.__zoomeye
