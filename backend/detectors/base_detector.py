from abc import ABC, abstractmethod
import os
from pathlib import Path

class BaseDetector(ABC):
    def __init__(self):
        self.name = None
    
    @property
    def plugin_path(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        path = Path(dir_path)
        project_path = path.parent.parent
        filepath = os.path.join(project_path, "plugins", self.name + ".yaml")
        return filepath

    @abstractmethod
    def process(self):
        pass
    
    def get_google_dorks(self):
        """
        Pobiera opjce google dorks z https://www.exploit-db.com/google-hacking-database po self.name
        problem - brak API
        """
        pass

    def get_exploit(self):
        """
        Pobiera liste exploitów z https://www.exploit-db.com/ po self.name
        problem - brak API
        """
        pass