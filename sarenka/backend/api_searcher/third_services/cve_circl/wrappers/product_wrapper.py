class ProductWrapper:
    def __init__(self, vendor, name, version, system):
        self.__vendor = vendor
        self.__name = name
        self.__version = version
        self.__system = system

    @property
    def vendor(self):
        return self.__vendor

    @property
    def name(self):
        return self.__name

    @property
    def version(self):
        return self.__version

    @property
    def system(self):
        return self.__system

    def to_dict(self):
        return {
            "vendor": self.vendor,
            "name": self.name,
            "version": self.version,
            "system": self.system
        }

    def __str__(self):
        return "vendor: {}\nname: {}\nversion: {}\nsystem: {}\n".format(
            self.vendor,
            self.name,
            self.version,
            self.system
        )

