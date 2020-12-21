import socket


class PortScanner:
    def __init__(self, ip_address:str, port:str):
        """
        Skaner portu - znacznie wolneijsza funckjonalność niż w nmapie.
        :param ip_address: adres ip hosta
        :param port: numer portu
        """
        self.host = ip_address
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.settimeout(5)

    def scan(self):
        result = []
        if self.socket.connect_ex((self.host, int(self.port))):
            result.append({self.port: "closed"})
        else:
            result.append({self.port: "open"})
        return result


if __name__ == "__main__":
    scanner = PortScanner("137.74.187.100", "21")
    print(scanner.scan())