import re

from analyzer.softwares.software_info_interface import SoftwareInfoInterface


class ImageMagick(SoftwareInfoInterface):
    """
    Klasa mająca informacje o konkentym sofcie
    docelowo dane będą z bazy
    tymczasowo na sztywno podaję dane
    """
    def __init__(self):
        super().__init__(
            vendor="ImageMagick",
            name="ImageMagick",
            repository="https://github.com/ImageMagick/ImageMagick/",
            software_website="https://imagemagick.org/",
        )

    def get_pattern(self):
        """
        Zwraca pattern sprawdzający wersje oprogramowania
        - SPECYFICZNE DLA KAZDEGO SOFTU - TRZEBA DANE DODAC RECZNIE !!!!
        """
        pattern = r"(before\s+and\s+\d+\.\d+\.\d+\-\d+( Q16)?)|(before\s+\d+\.\d+\.\d+\-\d+( Q16)?)|(\d+\.\d+\.\d+\-\d+( Q16)?\s+and\s+earlier)|(\d+\.\d+\.\d+\-\d+( Q16)?)|(before\s+\d+\.\d+\.\d+( Q16)?)|(\d+\.\d+\.\d+( Q16)?\s+and\s+earlier)|(\d+\.\d+\.\d+( Q16)?)"
        return pattern

    def get_released_versions(self):
        releases_link = self.repository + "releases"
        pass

    def __str__(self):
        return f"Vendor: {self.vendor}\nSoftware: {self.name}\nPattern: {self.pattern}"

if __name__ == "__main__":
    image_magick = ImageMagick()
