from django.conf import settings
USER_CREDENTIALS_DB = settings.USER_CREDENTIALS_DB_NAME

from api_searcher.models import CensysCredentialsModel

class CensysCredentialsError(Exception):
    """Zgłasza wyjątek gdy nie można utworzyć obiketu przechowujące dane użytkownika do seriwsu http://censys.io/"""
    def __init__(self, message=None, errors=None):
        super().__init__(message)
        self.errors = errors


class CensysCredentials:
    """Sinleton - Klasa przechowująca wymagane dane dla seriwsu trzeciego http://censys.io/.
    Daje także możliwość aktualizacji danych uwierzytelniających użytkownika np. w przypadku przekroczenia ilości
    wyszukiwań na darmowym koncie w serwisie."""
    __instance = None

    def __init__(self):
        if not CensysCredentials.__instance:
            credentials_obj = CensysCredentialsModel.objects.using(self.db_name).all().first()
            if not credentials_obj:
                credentials_obj = CensysCredentialsModel.objects.using(self.db_name).create()

            self.__base_url = credentials_obj.base_url
            self.__api_id = credentials_obj.api_id
            self.__secret = credentials_obj.secret
            self.__api_url = credentials_obj.api_url
        else:
            self.getInstance()

    @classmethod
    def getInstance(cls):
        """Metoda klasy wymaga dla klasy typu Singleton
        - zwraca instancję klasy, gwarantuje istnienie tylko jednego obiektu z danymi wuierzytleniajacmi użytkownika."""
        if not cls.__instance:
            cls.__instance = CensysCredentials()
        return cls.__instance


    @property
    def db_name(self):
        return USER_CREDENTIALS_DB

    @property
    def base_url(self):
        return self.__base_url

    @property
    def api_id(self):
        return self.__api_id

    def update_api_id(self, new_api_id):
        """Metoda do aktualizacji danych "API_ID" dla konta użytkownika do serwisu http://censys.io/ """
        if not new_api_id:
            raise CensysCredentialsError('Censys "API_ID" value is empty.')

        credentials_obj = CensysCredentialsModel.objects.using(self.db_name).all().first()
        credentials_obj.api_id = new_api_id
        credentials_obj.save()

        # aktualizacja danych obiektu
        self.__api_id = new_api_id

    @property
    def secret(self):
        return self.__secret

    def update_secret(self, new_secret):
        """Metoda niezbędne do aktualizacji danych "Secret" dla konta użytkownika do serwisu http://censys.io/ """
        if not new_secret:
            raise CensysCredentialsError('Censys "Secret" value is empty.')

        credentials_obj = CensysCredentialsModel.objects.using(self.db_name).all().first()
        credentials_obj.secret = new_secret
        credentials_obj.save()

        # aktualizacja danych obiektu
        self.__secret = new_secret

    @property
    def api_url(self):
        return self.__api_url