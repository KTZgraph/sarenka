from abc import ABC, abstractmethod

class BaseConnector(ABC):
    def __init__(self, data):
        self.__base_url = data.base_url
        self.__api_key = data.api_key
        self.__user = data.user

    @property
    def url(self):
        return self.__base_url

    @property
    def user(self):
        return self.__user

    @property
    def api_key(self):
        return self.__api_key
    
    @abstractmethod
    def search(query):
        pass
