"""
Moduł do przechowywania danych użytkownika takich jak klucze do serwisów,
które wymagają kont dla korzystania z ich api i/lub funkcjonalności.
"""
import json
from .censys_engine.censys_credentials import CensysCredentials
from .shodan_engine.shodan_credentials import ShodanCredentials
import os


class UserCredentialsError(Exception):
    """
    Zgłoszenie wyjąktu gdy są problemy z danymi użytkownika do serwisów trzecich.
    """
    def __init__(self, message=None, errors=None):
        super().__init__(message)
        self.errors = errors


class UserCredentials:
    """Singleton - Klasa przechowująca dane użytkownika do serwisów trzecich niezbędne do korzystania z ich funkcjonalności."""
    __instance = None
    __config_file = "user_credentials.json"

    @classmethod
    def get_config_file_path(cls):
        """Metoda klasy zwracajaca ścieżkę do pliku konfiguracyjnego użytkownika."""
        current_dir = os.path.dirname(__file__)
        return os.path.join(current_dir, cls.__config_file)

    @property
    def config_file_path(self):
        """Atrybut klasy zwracajacy ścieżkę do pliku z danymi uwierzytelniajacymi użytkownika."""
        return self.get_config_file_path()

    def __init__(self):
        if not UserCredentials.__instance:
            try:
                with open(self.config_file_path) as f:
                    data = json.load(f)
            except FileNotFoundError:
                raise UserCredentialsError("User credential file does not exist. "
                                           "Please create file sarenka/backend/api_searcher/search_engines/user_credentials.json "
                                           "or clone from repository https://github.com/pawlaczyk/sarenka")

            self.__censys = CensysCredentials(data.get("censys", None))
            self.__shodan = ShodanCredentials(data.get("shodan", None))
        else:
            self.getInstance()

    @classmethod
    def getInstance(cls):
        """Metoda klasy wymaga dla klasy typu Singleton
        - zwraca instancję klasy, gwarantuje istnienie tylko jednego obiektu z danymi wuierzytleniajacmi użytkownika."""
        if not cls.__instance:
            cls.__instance = UserCredentials()
        return cls.__instance

    @property
    def censys(self):
        """Atrybut zwracajacy dane uwierzytelniajace użytkownika dla serwisu http://censys.io/"""
        return self.__censys

    @property
    def shodan(self):
        """Atrybut zwracajacy dane uwierzytelniajace użytkownika dla serwisu https://shodan.io/"""
        return self.__shodan