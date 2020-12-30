class CensysCredentialsError(Exception):
    """Zgłasza wyjątek gdy nie można utworzyć obiketu przechowujące dane użytkownika do seriwsu http://censys.io/"""
    def __init__(self, message=None, errors=None):
        super().__init__(message)
        self.errors = errors


class CensysCredentials:
    """Klasa przechowująca wymagane dane dla seriwsu trzeciego http://censys.io/."""
    def __init__(self, data):
        if not data:
            raise CensysCredentialsError("No data to http://censys.io/ service. Please check "
                                         "sarenka\\backend\\api_searcher\\search_engines\\user_credentials.json file.")

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
            raise CensysCredentialsError(f'No data in "{info_tag}" for service http://censys.io/ service. Please check '
                                         f'sarenka\\backend\\api_searcher\\search_engines\\user_credentials.json file.')
