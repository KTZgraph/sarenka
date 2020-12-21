from common.dict_x import DictX


class DNSWrapper:
    def __init__(self, data):
        self.__lookup = DictX(data.get("lookup"))
        self.__names = self.get_names()

    def get_names(self):
        answers = self.__lookup.get("answers")
        names = []
        if answers:
            for answer in answers:
                names.append(answer.get("name"))

        return list(set(names)) #unikalne tylko 

    @property
    def names(self):
        return self.__names

    @property
    def is_resolves_correctly(self):
        return self.__lookup.get("resolves_correctly")    

    @property
    def is_support(self):
        return self.__lookup.get("support")    

    @property
    def is_open_resolver(self):
        return self.__lookup.get("open_resolver")    

    @property
    def is_erros(self):
        return self.__lookup.get("errors") if self.__lookup.get("errors") else None

    def __str__(self):
        return f"Names:{self.names}\nis_erros:{self.is_erros}\nis_resolves_correctly:{self.is_resolves_correctly}\nis_support:{self.is_support}\nis_open_resolver:{self.is_open_resolver}"