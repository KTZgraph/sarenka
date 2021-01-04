import re


class HostDetailsWrapper:
    """Klasa pomocnicza - wrapper parsujacy dane z serwisu https://www.shodan.io/."""

    def __init__(self, ip, host_details):
        self.__ip = ip
        self.__data = host_details

    @property
    def ip(self):
        """Atrybut zwracajacy adres ip hosta."""
        return self.__ip

    @property
    def data(self):
        return self.__data.get("data", [])

    @property
    def ports(self):
        """Atrybut klaasy zwracajacy informacje o portach."""
        return self.__data.get("ports", [])

    @property
    def http(self):
        """Atrybut zwracajacy infromacje o portach gdize wykosztyswany jest protokół http"""
        results = []
        for i in self.data:
            port = i.get("port", None)
            http = i.get("http", {})
            results.append({"port": port, "http": http})
        return results

    @property
    def html(self):
        """Atrybut zwracający dane html."""
        results = []
        for i in self.http:
            port = i.get("port", None)
            html_data = i.get("http", {})
            if port and html_data:
                results.append({"port": port, "html": html_data})
        return results

    @property
    def redirects(self):
        """Atrybut zwracajacy informacje o przekierowaniach do innych hostów"""
        results = []
        for i in self.html:
            port = i.get("port", None)
            html_data = i.get("html", None)
            if html_data and port:
                redirects = html_data.get("redirects", {})
                if port and redirects:
                    for r in redirects:
                        redirect_data = r.get("data", "")
                        pattern = r'https:\/\/\d+\.\d+\.\d+\.\d+\/*\w+\/*'  # TODO:
                        addresses = re.findall(pattern, redirect_data)
                        results.append({"port": port, "redirects": addresses})

        return results

    @property
    def to_json(self):
        response = {}
        response.update({"ip": self.ip})
        response.update({"ports": self.ports})
        response.update({"html": self.html})
        response.update({"redirects": self.redirects})
        return response
