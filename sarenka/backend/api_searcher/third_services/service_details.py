"""
Moduł do przechowywania danych szczegółowych takich jak adresy url do głównej strony jak i wybranych funckjonalności
dla serwisów trzeich, które nie wymagają uwierzytelniania od użytkownika.
"""
import json
import os

from .cve_circl.cve_circl_details import CveCirclDetails


class ServiceDetailsError(Exception):
    """
    Zgłoszenie wyjąktu gdy są problemy z danymi dla seriwsów trzecich nie wymagających uwierzytelniania użytkownika.
    """
    def __init__(self, message=None, errors=None):
        super().__init__(message)
        self.errors = errors


class ServiceDetails:
    """Singleton - klasa przechowujaca informacje o serwisach trzecich z których pobierane są dane"""
    __instance = None
    __config_file = "service_details.json"

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
        if not ServiceDetails.__instance:
            try:
                with open(self.config_file_path) as f:
                    data = json.load(f)
            except FileNotFoundError:
                raise ServiceDetailsError("Details for third part service not found."
                                           "Please create file sarenka/backend/api_searcher/search_engines/service_details.json "
                                           "or clone it from repository https://github.com/pawlaczyk/sarenka")
            self.__cve_circl = CveCirclDetails(data.get("cve_circl", None))

    @classmethod
    def getInstance(cls):
        """Metoda klasy wymaga dla klasy typu Singleton
        - zwraca instancję klasy, gwarantuje istnienie tylko jednego obiektu z danymi do serwisó trzeich."""
        if not cls.__instance:
            cls.__instance = ServiceDetails()
        return cls.__instance

    @property
    def cve_circl(self):
        """Atrybut klasy zwracaja szczegóły do serwisu https://cve.circl.lu/.
        Informacje niezbędnę by pobierać informacje z powyższego serwisu"""
        return self.__cve_circl