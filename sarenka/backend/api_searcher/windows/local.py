import subprocess


class LocalInfo:
    """
    Pobieranie lokalnych informacji o systemie i maszynie Windows.
    """
    @staticmethod
    def get_systeminfo():
        """
        Zwraca infromacje o systemie
        """
        value = subprocess.getoutput("systeminfo")
        value = value.split("\n")
        value = [i.strip() for i in value if i!=""]
        return {
            "systeminfo": value
        }

    def parse_data(self):
        data = self.get_systeminfo()

    @property
    def values(self):
        return {
            "local_info": self.get_systeminfo()
        }




if __name__ == "__main__":
    print(LocalInfo.get_systeminfo())
