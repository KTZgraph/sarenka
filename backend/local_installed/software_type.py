import enum

from analyzer.softwares.software_info_interface import SoftwareInfoInterface
from analyzer.softwares.imagemagick import ImageMagick

class SoftwareType(enum.Enum):
    Windows = "local_windows"
    Linux = "local_linux"
    Backend = "web_backend"
    Fontend = "web_frontend"


class WindowsSoftware:
    """
    Przechowuje informacje o konkrentej instalacji aplikacji np sciezke z wersja:
    Komputer\\HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\ImageMagick 7.0.10 Q16 (64-bit)_is1
    obiekty Tworzone podczas przegladania rejestrow Windowsa
    """
    __software_type = SoftwareType.Windows

    def __init__(self, software_info:SoftwareInfoInterface, 
                        registry_path:str, 
                        installed_version:str):

        self.__info = software_info
        self.__registry_path = registry_path
        self.__installed_version = installed_version

    @property
    def software_type(self):
        return self.__software_type

    @property
    def info(self):
        return self.__info

    @property
    def registry_path(self):
        return self.__registry_path
    
    @property
    def installed_version(self):
        return self.__installed_version

    @property
    def vendor(self):
        return self.__info.vendor

    @property
    def name(self):
        return self.__info.name

    @property
    def website(self):
        return self.__info.website

    @property
    def repository(self):
        return self.__info.repository

    def __str__(self):
        return f'Type: {self.software_type}\nVendor: {self.vendor}\nName: {self.name}\nWebsite: {self.website}\nWebsite: {self.repository}'


if __name__ == "__main__":
    print(SoftwareType.Windows)

    registry_path = "Komputer\\HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\ImageMagick 7.0.10 Q16 (64-bit)_is1"
    installed_version = "7.0.10 Q16"

    w = WindowsSoftware(ImageMagick(), registry_path, installed_version)
    print(w)