import json
import os

from .user_credentials import UserCredentials, UserCredentialsError


class UserCredentialsUpdaterError(Exception):
    """
    Zgłasza wyjątek gdy nie można zaktualizować dane użytkownika do serwisów trzeich.
    """
    def __init__(self, message=None, errors=None):
        super().__init__(message)
        self.errors = errors


class UserCredentialsUpdater:
    """Klasa umożlwiiajaca użytkownikowi dodanie wlasnych klucyz do serwisów trzecich, wymagających danych i kont do nich."""
    __user_credentials_file = "user_credentials.json"

    def __init__(self, user_data):
        self.__user_data = user_data
        self.user_credentials = UserCredentials()

    @classmethod
    def __get_config_file_path(cls):
        """Metoda klasy zwracajaca ścieżkę do pliku z danymi uwierzytelniajacymi użytkownika do serwisów trzecich."""
        current_dir = os.path.dirname(__file__)
        return os.path.join(current_dir, cls.__user_credentials_file)

    @property
    def config_file_path(self):
        """Atrybut klasy zwracający ściezkę do pliku konfiguracyjnego"""
        return self.__get_config_file_path()

    def __save_credentials_file(self, new_credentials):
        """Metoda zapisująca zaktualizowanego jsona jako plik z danymi uwiezytelniajacymi użytkownika."""
        with open(self.config_file_path, "w") as f:
            f.write(json.dumps(new_credentials, indent=4))

    def __credentials_file_to_dict(self):
        """Metoda pomocnicza - wczytuje plik z danymi użytkownika i zwraca je w postaci słwonika pythona."""
        with open(self.config_file_path) as f:
            credential_data = json.load(f)
        return credential_data

    def __update_censys_credentials(self):
        """Metoda pomocnicza aktualizująca dane uwierzytelniające użytkownika do serwisu http://censys.io/
        Aktualizuje obiekt przechowujący dane oraz plik konfiguracyjny."""
        try:
            new_api_id = self.__user_data.get("censys_API_ID", "")
            new_secret = self.__user_data.get("censys_Secret", "")

            self.user_credentials.censys.update_api_id(new_api_id)
            self.user_credentials.censys.update_secret(new_secret)

            credential_data = self.__credentials_file_to_dict()
            credential_data["censys"]["API_ID"] = new_api_id
            credential_data["censys"]["Secret"] = new_secret
            self.__save_credentials_file(credential_data)

        except Exception as ex:
            raise UserCredentialsUpdaterError(str(ex))

    def __update_shodan_credentials(self):
        """Metoda pomocnicza aktualizująca dane uwierzytelniające użytkownika do serwisu https://shodan.io/
        Aktualizuje obiekt przechowujący dane oraz plik konfiguracyjny."""
        try:
            new_shodan_user = self.__user_data.get("shodan_user", "")
            new_shodan_api_key= self.__user_data.get("shodan_api_key", "")

            self.user_credentials.shodan.update_user(new_shodan_user)
            self.user_credentials.shodan.update_api_key(new_shodan_api_key)

            credential_data = self.__credentials_file_to_dict()
            credential_data["shodan"]["user"] = new_shodan_user
            credential_data["shodan"]["api_key"] = new_shodan_api_key
            self.__save_credentials_file(credential_data)

        except Exception as ex:
            raise UserCredentialsUpdaterError(str(ex))

    def update(self):
        """Metoda aktualizująca i zapisujaca do pliku dane uwierzytelniające użytkownika do serwisów trzeich,
        które udostępniaja swoje dane tylko po utworzeniu konta z uniklanym kluczem przypisanym użytkownikowi."""
        self.__update_censys_credentials()
        try:
            self.__update_shodan_credentials()
        except Exception as ex:
            print("\n\n\n\n")
            print(ex)
            print(type(ex))