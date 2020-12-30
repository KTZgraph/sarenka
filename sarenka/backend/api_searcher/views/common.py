import ipaddress
import socket


class Common:
    """Klasa pomocnicza zwracajaca najcześciej używane funkcje przez widoki api_searcher."""
    def __init__(self, request):
        self.request = request

    @property
    def host_address(self):
        """Atrybut zwrcacający adres hosta na którym uruchomiony jest backend aplikacji SARENKA."""
        return self.__get_host_address()

    def __get_host_address(self):
        """
        Zwraca adres do hosta na którym uruchomiony jest serwer backend aplikacji.
        Uwzglednienia protokoły HTTP oraz HTTPS.
        Użycie - generpowanie urli do wewnątrz aplikacji przez widoki Django w api_searcher.
        """
        host_address = self.request.get_host()
        if self.request.is_secure():
            address = "https://" + host_address
        else:
            address = "http://"+ host_address
        return address

    @staticmethod
    def is_ipv4(host:str):
        """Metoda statyczna sprawdzająca czy podano adres ip czy domenę."""
        try:
            ipaddress.IPv4Network(host)
            return True
        except ValueError:
            return False

    @staticmethod
    def get_ip_addres(host):
        """Metoda statyczna zwracająca adres ip adress hosta."""
        if Common.is_ipv4(host):
            return host
        return socket.gethostbyname(host)