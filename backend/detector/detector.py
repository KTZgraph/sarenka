import os
from pathlib import Path
import yaml
import pprint


class DetectorNotFoundError(Exception):
    """ 
    Zgłasza wyjatek gdy nie istnieje plik detektora
    """
    def __init__(self, message=None, errors=None):
        super().__init__(message)
        self.errors = errors


class DetectorKeyNotFoundError(Exception):
    """
    Zgłasza wyjątki gdy brak klucza w yamlu
    """
    def __init__(self, message =None, errors=None):
        super.__init__(message)
        self.errors = errors


class Detector:
    """
    Klasa przechowująca dane o detekcji konkretnego softu na podstawie plików yaml
    """
    obligatory_keys = [
        
    ]

    def __init__(self, name):
        """
        Jak sensownie tworyzć klasę z pliku yaml?
        """
        self.name = name
        self._data = self.data
    
    def _get_value(self, key):
        if key not in self.data:
            raise SoftwareDetectorKeyNotFoundError(f'"{key}" is obligatory')
        return self._data[key]

    @property
    def plugin_path(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        path = Path(dir_path)
        project_path = path.parent.parent
        filepath = os.path.join(project_path, "detectors", self.name + ".yaml")
        return filepath

    @property
    def data(self):
        try:
            with open(self.plugin_path) as f:
                plugin_data = yaml.safe_load(f)
        except FileNotFoundError:
            raise DetectorNotFoundError(f"File {self.plugin_path} not found.")
        return plugin_data
    
    @property
    def software(self):
        return self._get_value("software")
    
    @property
    def names(self):
        return self._get_value("names")

    @property
    def cve_details_url(self):
        return self._get_value("cve_details_url")
    
    @property
    def description(self):
        return self._get_value("description")
    
    @property
    def formely_name(self):
        return self._get_value("formely_name")
    
    @property
    def vendor_name(self):
        return self._get_value("vendor_name")

    @property
    def vendor_url(self):
        return self._get_value("vendor_url")

    @property
    def repository(self):
        return self._get_value("repository")

    @property
    def releases(self):
        return self._get_value("releases")

    @property
    def text_title(self):
        return self._get_value("text_title")

    @property
    def text_404(self):
        return self._get_value("text_404")

    @property
    def text_characteristic(self):
        return self._get_value("text_characteristic")

    @property
    def regex_patterns(self):
        return self._get_value("regex_patterns")

    @property
    def search_shodan(self):
        return self._get_value("search_shodan")

    @property
    def search_censys(self):
        return self._get_value("search_censys")

    @property
    def google_dorks(self):
        return self._get_value("google_dorks")

    @property
    def favicon_url(self):
        return self._get_value("favicon_url")

    @property
    def protocols(self):
        return self._get_value("protocols")
    
    @property
    def ports(self):
        return self._get_value("ports")
    
    @property
    def files(self):
        return self._get_value("files")
    
    @property
    def available_os(self):
        return self._get_value("available_os")

    @property
    def software_type(self):
        return self._get_value("software_type")

    @property
    def download_link(self):
        return self._get_value("download_link")

    @property
    def exploits(self):
        return self._get_value("exploits")
    
    @property
    def docker_image(self):
        return self._get_value("docker_image")

    @property
    def related_softwares(self):
        return self._get_value("related_softwares")

    @property
    def fingerprint(self):
        return self._get_value("fingerprint")

    @property
    def banner_example(self):
        return self._get_value("banner_example")
    
    @property
    def windows_registry_path(self):
        return self._get_value("windows_registry_path")

    @property
    def linux_package(self):
        return self._get_value("linux_package")

    @property
    def dependencies(self):
        return self._get_value("dependencies")

    @property
    def to_json(self):
        result = {}
        return result
        
    def __str__(self):
        return "trzeba recznie ldnie poskladac ;/"


    def process(self):
        pass
    
    def get_google_dorks(self):
        """
        Pobiera opjce google dorks z https://www.exploit-db.com/google-hacking-database po self.name
        problem - brak API
        """
        pass

    def get_exploit(self):
        """
        Pobiera liste exploitów z https://www.exploit-db.com/ po self.name
        problem - brak API
        """
        pass

if __name__ == "__main__":
    software_detector = SoftwareDetector("apache")
    print(software_detector.search_shodan)
    print("TUUUUUUUUUUUUUUUUUUUUUUUUU")
    # print(software_detector.to_json)
    print(software_detector)