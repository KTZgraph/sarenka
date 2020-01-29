from typing import Dict, Tuple, Sequence, List, NoReturn
from abc import ABC, abstractmethod

from connectors.base_connector import BaseConnector

class ConnectorInterface(BaseConnector):
    def __init__(self, data):
        super().__init__(data)

    @abstractmethod
    def host(self, ip, ports=[]):
        pass
