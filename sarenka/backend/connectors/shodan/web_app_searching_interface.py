from abc import ABC, abstractmethod

class WebAppSearchingInterface(ABC):
    
    def __init__(self, host_wrapper):
        self.host = host_wrapper

    @abstractmethod
    def search_version(self):
        pass
