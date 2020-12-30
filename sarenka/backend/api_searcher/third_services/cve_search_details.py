class CVESearchDetailsError(Exception):
    """Klasa zgłaszajca wyjątek gdy nie można stworzyć obiektu przechowujacego szczegółowe dane do serwisu trzeciego
    https://cve.circl.lu"""
    def __init__(self, message=None, errors=None):
        super().__init__(message)
        self.errors = errors


class CVESearchDetails:
    """Klasa przechowuje szczegółowe dane do serwiu trzeciego https://cve.circl.lu oraz jego specyficznych urli.
    Serwis nie wymagaja uwierzytelnienia użytkownika"""

    def __init__(self, data):
        if not data:
            raise CVESearchDetailsError("No data about https://cve.circl.lu service. Please check "
                                         "sarenka\\backend\\api_searcher\\third_services\\details.json file.")
        self.__base_url = data["base_url"]
        self.__cve = data["cve"]
        self.__vendor = data["vendor"]
        self.__last = data["last"]
        self.__db_info = data["db_info"]

    def __set_data(self, info_tag:str):
        """Metoda pomocnicza zwracajaca wybrane ifnormacje do seriwsu http://censys.io/ z pliku user_credentials.json
        :param: info_tag
        """
        if self.data.get(info_tag, None):
            return self.data[info_tag]
        else:
            raise CVESearchDetailsError(f'No data in "{info_tag}" for  https://cve.circl.lu service. Please check '
                                         f'sarenka\\backend\\api_searcher\\third_services\\details.json file.')