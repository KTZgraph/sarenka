from typing import Dict, Tuple, Sequence, List, NoReturn
from abc import ABC, abstractmethod

class SoftwareInfoInterface(ABC):
    """
    Bazowe informacje o konkrentym sofcie, uzuełnianie ręcznie / z bazy
    pattern regexów na początku z pliku jsona docelowo te regexe dla wersji trzeba będzie trzymać w bazie
    na razie skupiamy się na oprogramowaniu; ale jak będziemy umieli znaleść jakieś urzadzenia np. routery to też dodamy

    Odpowiedzialnością klasy jest przechowywanie informacji o specyfinym sofcie
    """

    def __init__(self, vendor, name, repository, website=""):
        self.__vendor = vendor
        self.__name = name
        self.__repository = repository 
        self.__website = website
        self.__pattern = self.get_pattern()
        self.__released_version = self.get_released_versions()

    @property
    def vendor(self):
        return self.__vendor

    @property
    def name(self):
        return self.__name
    
    @property
    def website(self):
        return self.__website

    @property
    def repository(self):
        return self.__repository
    
    @property
    def pattern(self):
        return self.__pattern

    @property
    def released_version(self):
        return self.__released_version

    @abstractmethod
    def get_pattern(self):
        pass

    @abstractmethod
    def get_released_versions(self):
        """
        W github często sa informacje o wersjach jakie wydano; można w ten sposób porównywac 
        znalezione wersje regexem i sprawdzać czy logicznie należą do wydanych przez vendora wersji
        Przykład informacji o wersji: https://github.com/ImageMagick/ImageMagick/releases
        """
        pass

    def __str__(self):
        return f'Vendor: {self.vendor}\nName: {self.name}\n Website: {self.website}'
