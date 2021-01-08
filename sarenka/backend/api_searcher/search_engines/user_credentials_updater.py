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

    def __init__(self, user_data):
        self.__user_data = user_data
        self.user_credentials = UserCredentials()

    @property
    def user_data(self):
        return self.__user_data

    def __update_censys_credentials(self):
        """Metoda pomocnicza aktualizująca dane uwierzytelniające użytkownika do serwisu http://censys.io/
        Aktualizuje obiekt przechowujący dane oraz plik konfiguracyjny."""

        credentials_data = self.user_data["censys"]
        new_api_id = credentials_data.get("API_ID", "")
        new_secret = credentials_data.get("Secret", "")

        self.user_credentials.censys.update_api_id(new_api_id)
        self.user_credentials.censys.update_secret(new_secret)

    def __update_shodan_credentials(self):
        """Metoda pomocnicza aktualizująca dane uwierzytelniające użytkownika do serwisu https://shodan.io/
        Aktualizuje obiekt przechowujący dane oraz plik konfiguracyjny."""
        credentials_data = self.user_data["shodan"]
        new_shodan_user = credentials_data.get("user", "")
        new_shodan_api_key= credentials_data.get("api_key", "")

        self.user_credentials.shodan.update_user(new_shodan_user)
        self.user_credentials.shodan.update_api_key(new_shodan_api_key)

    def update(self):
        """Metoda aktualizująca i zapisujaca do pliku dane uwierzytelniające użytkownika do serwisów trzeich,
        które udostępniaja swoje dane tylko po utworzeniu konta z uniklanym kluczem przypisanym użytkownikowi."""
        try:
            self.__update_censys_credentials()
            self.__update_shodan_credentials()
        except Exception as ex:
            raise UserCredentialsUpdaterError(str(ex))

