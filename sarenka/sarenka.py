""""
Moduł odpwoaidajacy za budowanie środowiska, uruchamianie aplikacji, aktualizacja feedów i konserwację.
Skrypt ukrywa komendy przed użytkownikiem który jest nie ogarnięty. Proste tak by nauczyciel akademicki dał radę.
"""
import os
import sys
IS_WINDOWS = sys.platform.startswith('win')
IS_LINUX = sys.platform.startswith('linux') # linux or linux2 (*)


class SarenkaBuildError(Exception):
    """
    Zgłasza wyjątek gdy nie można zbudować aplikacji SARENKA.
    """
    def __init__(self, message=None, errors=None):
        super().__init__(message)
        self.errors = errors


class SarenkaRunserverError(Exception):
    """
    Zgłasza wyjątek gdy nie można zbudować aplikacji SARENKA.
    """
    def __init__(self, message=None, errors=None):
        super().__init__(message)
        self.errors = errors


class SarenkaFeedError(Exception):
    """
    Zgłasza wyjątek gdy nie można zbudować aplikacji SARENKA.
    """
    def __init__(self, message=None, errors=None):
        super().__init__(message)
        self.errors = errors


class SarekaMaintenanceError(Exception):
    """
    Zgłasza wyjątek gdy nie można zbudować aplikacji SARENKA.
    """
    def __init__(self, message=None, errors=None):
        super().__init__(message)
        self.errors = errors


class SarenkaInfoError(Exception):
    """
    Zgłasza wyjątek gdy nie można zbudować aplikacji SARENKA.
    """
    def __init__(self, message=None, errors=None):
        super().__init__(message)
        self.errors = errors


class SarenkaBuild:
    """Klasa odpowiadajaca za budowanie aplikacji """
    def __init__(self, verbose=False):
        self.is_verbose = verbose

    def create_env(self):
        if self.is_verbose:
            print("creating env")

    def install_requirements(self):
        """Instaluje wymagane biblioteki w zależności od systemu operacyjnego na jakim ma być uruchamiona aplikacja."""
        if IS_WINDOWS:
            if self.is_verbose:
                print("Installing requirements for Windows")
        elif IS_LINUX:
            if self.is_verbose:
                print("Installing requirements for Linux")
        else:
            raise



    def build_fontend(self):
        if self.is_verbose:
            print("Building React fontent - npm run build ")



class SarenkaRunserver:
    """Klasa odpowiadajaca za uruchomienie aplikacji"""
    def __init__(self, verbose=False):
        self.is_verbose = verbose

    def create_env(self):
        if self.is_verbose:
            print("Starting Django server")


class SarenkaFeed:
    def __init__(self, verbose=False):
        self.is_verbose = verbose

        dir_path = os.path.dirname(__file__)

    def get_feed_info(self):
        pass




class SarekaMaintenance:
    def __init__(self, verbose=False):
        self.is_verbose = verbose


class SarenkaInfo:
    def __init__(self):
        result = {}

    @staticmethod
    def __get_authors():
        return {
            "Dominika Pawlaczyk": "https://github.com/pawlaczyk/",
            "Michał Pawlaczyk": "https://github.com/michalpawlaczyk",
            "Karolina Słonka": "https://github.com/k-slonka"
        }

    @staticmethod
    def get_feeds_info():
        pass

    @staticmethod
    def __get_project_info():
        return {
            "repository": "https://github.com/pawlaczyk/sarenka/",
            "package": "https://pypi.org/project/sarenka/",
            "maintainers" : "Dominika Pawlaczyk",
            "contact": "https://github.com/pawlaczyk",
            "documentation": "https://pawlaczyk.github.io/sarenka/",
            "license": "MIT",
            "look": [
                "https://www.facebook.com/ncybersec/posts/1671427243027993",
                "https://www.instagram.com/p/CI8tXMNg3yI/",
                "https://securityonline.info/sarenka-obtaining-and-understanding-attack-surface/",
                "https://haxf4rall.com/2020/12/30/sarenka-obtaining-and-understanding-attack-surface/",
                "http://hackdig.com/12/hack-245463.htm"
            ]
        }