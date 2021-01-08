from api_searcher.models import ShodanCredentailsModel


class ShodanCredentialsError(Exception):
    """Zgłasza wyjątek gdy nie można utworzyć obiketu przechowujące dane użytkownika do seriwsu https://shodan.io/"""
    def __init__(self, message=None, errors=None):
        super().__init__(message)
        self.errors = errors


class ShodanCredentials:
    """Klasa przechowująca wymagane dane dla seriwsu trzeciego https://shodan.io/.
    Daje także możliwość aktualizacji danych uwierzytelniających użytkownika np. w przypadku przekroczenia ilości
    wyszukiwań na darmowym koncie w serwisie."""

    def __init__(self, credentials_db_name:str):
        print("self.credentials_db_name: ", credentials_db_name)
        self.__db_name = credentials_db_name

        credentials_obj = ShodanCredentailsModel.objects.using(self.credentials_db_name).all().first()
        if not credentials_obj:
            credentials_obj = ShodanCredentailsModel.objects.using(self.credentials_db_name).create()

        self.__base_url = credentials_obj.base_url
        self.__api_key = credentials_obj.api_key
        self.__user = credentials_obj.user


    @property
    def credentials_db_name(self):
        return self.__db_name

    @property
    def base_url(self):
        return self.__base_url

    @property
    def api_key(self):
        return self.__api_key

    def update_api_key(self, new_api_key):
        """Metoda do aktualizacji danych "user" dla konta użytkownika do serwisu https://shodan.io/ """
        credentials_obj = ShodanCredentailsModel.objects.using(self.credentials_db_name).all().first()
        credentials_obj.api_key = new_api_key
        credentials_obj.save()

        # aktualizacja danych obiektu
        self.__api_key = new_api_key

    @property
    def user(self):
        return self.__user

    def update_user(self, new_user):
        """Metoda do aktualizacji danych "api_key" dla konta użytkownika do serwisu https://shodan.io/"""
        credentials_obj = ShodanCredentailsModel.objects.using(self.credentials_db_name).all().first()
        credentials_obj.user = new_user
        credentials_obj.save()

        # aktualizacja danych obiektu
        self.__user = new_user
