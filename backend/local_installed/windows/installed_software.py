class InstalledSoftware:
    def __init__(self, data):
        self.__name = data.get("DisplayName", None)
        self.__location = data.get("InstallLocation", None)
        self.__version = data.get("DisplayVersion", None)
        self.__vendor = data.get("Publisher", None)
        self.__date = data.get("InstallDate", None)

    @property
    def name(self):
        return self.__name

    @property
    def location(self):
        return self.__location

    @property
    def version(self):
        return self.__version

    @property
    def vendor(self):
        return self.__vendor

    @property
    def date(self):
        return self.__date

    def __str__(self):
        return f'Name: {self.name}\nLocation: {self.location}\nVersion: {self.version}\nVendor: {self.vendor}\nInstallation date: {self.date}\n'

    @property
    def to_dict(self):
        return {
            "name": self.name,
            "location": self.location,
            "version": self.version,
            "date": self.date,
            "vendor": self.vendor
        }
