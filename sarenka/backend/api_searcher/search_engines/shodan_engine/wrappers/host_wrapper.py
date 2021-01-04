class HostWrapper:
    """Klasa pomocnicza - wrapper na dane shodana o zwróconej liscie hostów.
    W zwracanych danych jest więcej hostów kosztem mniejszej ilości szczegółów o hoście"""

    def __init__(self, shodan_host_data, query):
        self.__data = shodan_host_data
        self.__query = query

    def __str__(self):
        return f'ip: {self.ip}\tport:{self.port}\n'

    @property
    def query(self):
        return self.__query

    @property
    def data(self):
        return self.__data.get("data", {})

    @property
    def ip(self):
        return self.__data.get("ip_str", {})

    @property
    def http(self):
        return self.__data.get("http", {})

    @property
    def html(self):
        return self.http.get("html", {})

    @property
    def port(self):
        return self.__data.get("port", {})