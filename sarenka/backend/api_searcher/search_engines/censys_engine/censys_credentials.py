from api_searcher.models import CensysCredentailsModel

class CensysCredentialsError(Exception):
    """Zgłasza wyjątek gdy nie można utworzyć obiketu przechowujące dane użytkownika do seriwsu http://censys.io/"""
    def __init__(self, message=None, errors=None):
        super().__init__(message)
        self.errors = errors


class CensysCredentials:
    """Klasa przechowująca wymagane dane dla seriwsu trzeciego http://censys.io/.
    Daje także możliwość aktualizacji danych uwierzytelniających użytkownika np. w przypadku przekroczenia ilości
    wyszukiwań na darmowym koncie w serwisie."""

    def __init__(self, credentials_db_name:str):
        # obiekt bazy danych z danymi uwierzytelniajacymi użytkownika
        self.__db_name = credentials_db_name

        credentials_obj = CensysCredentailsModel.objects.using(self.credentials_db_name).all().first()
        if not credentials_obj:
            credentials_obj = CensysCredentailsModel.objects.using(self.credentials_db_name).create()

        self.__base_url = credentials_obj.base_url
        self.__api_id = credentials_obj.api_id
        self.__secret = credentials_obj.secret
        self.__api_url = credentials_obj.api_url

    @property
    def credentials_db_name(self):
        return self.__db_name

    @property
    def base_url(self):
        return self.__base_url

    @property
    def api_id(self):
        return self.__api_id

    def update_api_id(self, new_api_id):
        """Metoda do aktualizacji danych "API_ID" dla konta użytkownika do serwisu http://censys.io/ """
        credentials_obj = CensysCredentailsModel.objects.using(self.credentials_db_name).first()
        credentials_obj.api_id = new_api_id
        credentials_obj.save()

        # aktualizacja danych obiektu
        self.__api_id = new_api_id

    @property
    def secret(self):
        return self.__secret

    def update_secret(self, new_secret):
        """Metoda niezbędne do aktualizacji danych "Secret" dla konta użytkownika do serwisu http://censys.io/ """
        credentials_obj = CensysCredentailsModel.objects.using(self.credentials_db_name).all().first()
        credentials_obj.secret = new_secret
        credentials_obj.save()

        # aktualizacja danych obiektu
        self.__secret = new_secret

    @property
    def api_url(self):
        return self.__api_url