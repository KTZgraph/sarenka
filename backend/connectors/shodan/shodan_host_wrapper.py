from typing import Dict, Tuple, Sequence, List, NoReturn

class ShodanHostWrapper:
    """Easier way to get day from dictionary returned by shodan api"""
    def __init__(self, shodan_host):
        self.__data = shodan_host
    
    @property
    def data(self):
        return self.__data.get("data",{})

    @property
    def ip(self):
        return self.__data.get("ip_str",{})

    @property
    def http(self):
        return self.__data.get("http", {})

    @property
    def html(self):
        return self.http.get("html", {})

    @property
    def port(self):
        return self.__data.get("port", {})