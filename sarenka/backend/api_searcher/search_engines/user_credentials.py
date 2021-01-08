"""
Moduł do przechowywania danych użytkownika takich jak klucze do serwisów,
które wymagają kont dla korzystania z ich api i/lub funkcjonalności.
"""
from .censys_engine.censys_credentials import CensysCredentials, CensysCredentialsError
from .shodan_engine.shodan_credentials import ShodanCredentials, ShodanCredentialsError


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

    def __init__(self):
        if not UserCredentials.__instance:

            try:
                self.__censys = CensysCredentials()
            except CensysCredentialsError as ex:
                raise UserCredentialsError(str(ex))
            try:
                self.__shodan = ShodanCredentials()
            except ShodanCredentialsError as ex:
                raise UserCredentialsError(str(ex))
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