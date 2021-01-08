from django.conf import settings
USER_CREDENTIALS_DB = settings.USER_CREDENTIALS_DB_NAME

from api_searcher.models import ShodanCredentialsModel


class ShodanCredentialsError(Exception):
    """Zgłasza wyjątek gdy nie można utworzyć obiketu przechowujące dane użytkownika do seriwsu https://shodan.io/"""
    def __init__(self, message=None, errors=None):
        super().__init__(message)
        self.errors = errors


class ShodanCredentials:
    """Singleton - Klasa przechowująca wymagane dane dla seriwsu trzeciego https://shodan.io/.
    Daje także możliwość aktualizacji danych uwierzytelniających użytkownika np. w przypadku przekroczenia ilości
    wyszukiwań na darmowym koncie w serwisie."""

    __instance = None

    def __init__(self):
        if not ShodanCredentials.__instance:
            credentials_obj = ShodanCredentialsModel.objects.using(self.db_name).all().first()
            if not credentials_obj:
                credentials_obj = ShodanCredentialsModel.objects.using(self.db_name).create()

            self.__base_url = credentials_obj.base_url
            self.__api_key = credentials_obj.api_key
            self.__user = credentials_obj.user
        else:
            self.getInstance()

    @classmethod
    def getInstance(cls):
        """Metoda klasy wymaga dla klasy typu Singleton
        - zwraca instancję klasy, gwarantuje istnienie tylko jednego obiektu z danymi wuierzytleniajacmi użytkownika."""
        if not cls.__instance:
            cls.__instance = ShodanCredentials()
        return cls.__instance

    @property
    def db_name(self):
        return USER_CREDENTIALS_DB

    @property
    def base_url(self):
        return self.__base_url

    @property
    def api_key(self):
        return self.__api_key

    def update_api_key(self, new_api_key):
        """Metoda do aktualizacji danych "user" dla konta użytkownika do serwisu https://shodan.io/ """
        if not new_api_key:
            raise ShodanCredentialsError('Shodan "api_key" value is empty.')

        credentials_obj = ShodanCredentialsModel.objects.using(self.db_name).all().first()
        credentials_obj.api_key = new_api_key
        credentials_obj.save()

        # aktualizacja danych obiektu
        self.__api_key = new_api_key

    @property
    def user(self):
        return self.__user

    def update_user(self, new_user):
        """Metoda do aktualizacji danych "api_key" dla konta użytkownika do serwisu https://shodan.io/"""
        if not new_user:
            raise ShodanCredentialsError('Shodan "user" value is empty.')

        credentials_obj = ShodanCredentialsModel.objects.using(self.db_name).all().first()
        credentials_obj.user = new_user
        credentials_obj.save()

        # aktualizacja danych obiektu
        self.__user = new_user

