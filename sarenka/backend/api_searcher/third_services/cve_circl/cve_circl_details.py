class CveCirclDetailsError(Exception):
    """Klasa zgłaszajca wyjątek gdy nie można stworzyć obiektu przechowujacego szczegółowe dane do serwisu trzeciego
    https://cve.circl.lu"""
    def __init__(self, message=None, errors=None):
        super().__init__(message)
        self.errors = errors


class CveCirclDetails:
    """Klasa przechowuje szczegółowe dane do serwiu trzeciego https://cve.circl.lu oraz jego specyficznych urli.
    Serwis nie wymagaja uwierzytelnienia użytkownika"""

    def __init__(self, data):
        if not data:
            raise CveCirclDetailsError("No data about https://cve.circl.lu service. Please check "
                                         "sarenka\\backend\\api_searcher\\third_services\\details.json file.")
        self.__base_url = self.__set_data("base_url")
        self.__cve = self.__set_data("cve")
        self.__db_info = self.__set_data("db_info")
        self.__last = self.__set_data("last")
        self.__vendor = self.__set_data("vendor")


    def __set_data(self, info_tag:str):
        """Metoda pomocnicza zwracajaca wybrane ifnormacje do seriwsu http://censys.io/ z pliku user_credentials.json
        :param: info_tag
        """
        if self.data.get(info_tag, None):
            return self.data[info_tag]
        else:
            raise CveCirclDetailsError(f'No data in "{info_tag}" for https://cve.circl.lu service. Please check '
                                         f'sarenka\\backend\\api_searcher\\third_services\\details.json file.')

    @property
    def base_url(self):
        return self.__base_url

    @property
    def cve(self):
        return self.__cve

    @property
    def db_info(self):
        return self.__db_info

    @property
    def vendor(self):
        return self.__vendor

    @property
    def last(self):
        return self.__last