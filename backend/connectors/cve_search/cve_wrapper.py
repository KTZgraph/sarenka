from common.converter import Converter
from .cve_parser import CVEParser

class CveWrapper:
    def __init__(self, data):
        self.__cve = CVEParser.cve(data) #kod podatności
        self.__cvss_vector = CVEParser.cvss_vector(data)
        self.__complexity = CVEParser.complexity(data)
        self.__authentication = CVEParser.authentication(data)
        self.__vector = CVEParser.vector(data)
        self.__cvss = CVEParser.cvss(data) #poziom zagrożenia
        self.__cwe = CVEParser.cwe(data)
        self.__title = CVEParser.title(data)
        self.__products = CVEParser.products(data)
        #impact - triada CIA
        self.__availability = CVEParser.availability(data)
        self.__confidentiality = CVEParser.confidentiality(data)
        self.__integrity = CVEParser.integrity(data)
        self.__summary = CVEParser.summary(data)

    @property
    def cve(self):
        return self.__cve

    @property
    def cvss_vector(self):
        return self.__cvss_vector

    @property
    def complexity(self):
        return self.__complexity

    @property
    def authentication(self):
        return self.__authentication

    @property
    def vector(self):
        return self.__vector

    @property
    def cvss(self):
        return self.__cvss 

    @property
    def cwe(self):
        return self.__cwe

    @property
    def title(self):
        return self.__title

    @property
    def products(self):
        return self.__products

    @property
    def availability(self):
        return self.__availability

    @property
    def confidentiality(self):
        return self.__confidentiality

    @property
    def summary(self):
        return self.__summary 

    def __str__(self):
        return f'CVE: {self.cve}'

    def to_dict(self):
        return {
            "cve" : self.cve,
            "cvss_vector" : self.cvss_vector,
            "complexity" : self.complexity,
            "authentication": self.authentication,
            "vector": self.vector,
            "cvss": self.cvss,
            "cwe": self.cwe,
            "title": self.title,
            "availability": self.availability,
            "confidentiality": self.confidentiality,
            "products": [p.to_dict() for p in self.products],
            "summary": self.summary
        }

