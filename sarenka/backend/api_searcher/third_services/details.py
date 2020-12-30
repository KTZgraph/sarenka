"""
Moduł do przechowywania danych szczegółowych takich jak adresy url do głównej strony jak i wybranych funckjonalności
dla serwisów trzeich, które nie wymagają uwierzytelniania od użytkownika.
"""
import json

from .api_searcher.third_services.cve_circl.cve_circl_details import CveCirclDetails

class DetailsError(Exception):
    """
    Zgłoszenie wyjąktu gdy są problemy z danymi dla seriwsów trzecich nie wymagających uwierzytelniania użytkownika.
    """
    def __init__(self, message=None, errors=None):
        super().__init__(message)
        self.errors = errors


class Details:
    """Singleton - klasa przechowujaca informacje o serwisach trzecich z których pobierane są dane"""
    __instance = None
    __config_file = "details.json"

    def __init__(self):
        if not Details.__instance:
            try:
                with open(self.__config_file) as f:
                    data = json.load(f)
            except FileNotFoundError:
                raise DetailsError("Details for third part service not found."
                                           "Please create file sarenka/backend/api_searcher/search_engines/user_credentials.json "
                                           "or clone it from repository https://github.com/pawlaczyk/sarenka")
            self.__cve_circl = CveCirclDetails(data.get("cve_circl"))