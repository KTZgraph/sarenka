class CensysCredentialsError(Exception):
    """Zgłasza wyjątek gdy nie można utworzyć obiketu przechowujące dane użytkownika do seriwsu http://censys.io/"""
    def __init__(self, message=None, errors=None):
        super().__init__(message)
        self.errors = errors


class CensysCredentials:
    """Klasa przechowująca wymagane dane dla seriwsu trzeciego http://censys.io/.
    Daje także możliwość aktualizacji danych uwierzytelniających użytkownika np. w przypadku przekroczenia ilości
    wyszukiwań na darmowym koncie w serwisie."""

    def __init__(self, data):
        if not data:
            raise CensysCredentialsError("No data to http://censys.io/ service. Please check "
                                         "sarenka\\backend\\api_searcher\\search_engines\\user_credentials.json file.")
        self.data = data
        self.__base_url = self.__set_data("base_url")
        self.__api_id = self.__set_data("API_ID")
        self.__secret = self.__set_data("Secret")
        self.__api_url = self.__set_data("API_URL")

    def __set_data(self, info_tag:str):
        """Metoda pomocnicza zwracajaca wybrane ifnormacje do seriwsu http://censys.io/ z pliku user_credentials.json
        :param: info_tag
        """
        if self.data.get(info_tag, None):
            return self.data[info_tag]
        else:
            raise CensysCredentialsError(f'No data in "{info_tag}" for http://censys.io/ service. Please check '
                                         f'sarenka\\backend\\api_searcher\\search_engines\\user_credentials.json file.')
    @property
    def base_url(self):
        return self.__base_url

    @property
    def api_id(self):
        return self.__api_id

    def update_api_id(self, value):
        """Metoda do aktualizacji danych "API_ID" dla konta użytkownika do serwisu http://censys.io/ """
        self.__api_id = value

    @property
    def secret(self):
        return self.__secret

    def update_secret(self, value):
        """Metoda niezbędne do aktualizacji danych "Secret" dla konta użytkownika do serwisu http://censys.io/ """
        self.__secret = value

    @property
    def api_url(self):
        return self.__api_url