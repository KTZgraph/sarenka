""""
Moduł odpwoaidajacy za budowanie środowiska, uruchamianie aplikacji, aktualizacja feedów i konserwację.
Skrypt ukrywa komendy przed użytkownikiem który jest nie ogarnięty. Proste tak by nauczyciel akademicki dał radę.

Kopiowanie plików
┌──────────────────┬────────┬───────────┬──────────┬────────────────┐
│     Function     │ Copies │   Copies  │ Use file │   Destination  │
│                  │metadata│permissions│  object  │may be directory│
├──────────────────┼────────┼───────────┼──────────┼────────────────┤
│shutil.copy       │   No   │    Yes    │    No    │      Yes       │
│shutil.copyfile   │   No   │     No    │    No    │       No       │
│shutil.copy2      │  Yes   │    Yes    │    No    │      Yes       │
│shutil.copyfileobj│   No   │     No    │   Yes    │       No       │
└──────────────────┴────────┴───────────┴──────────┴────────────────┘
"""
import os
from sys import platform
import json
from shutil import copy2, rmtree
from time import perf_counter
import subprocess

IS_WINDOWS = platform.startswith('win')
IS_LINUX = platform.startswith('linux')  # linux or linux2 (*)


class SarenkaBuildError(Exception):
    """
    Zgłasza wyjątek gdy nie można zbudować aplikacji SARENKA.
    """

    def __init__(self, message=None, errors=None):
        super().__init__(message)
        self.errors = errors


class SarenkaHelper:
    """Klasa pomocnicza zawierająca ścieżki do plików, oraz listy danych niezbędnych do zbudowania aplikacji."""

    def __init__(self):
        self.__current_dir_path = os.path.dirname(os.path.realpath(__file__))

        self.__feed_folder_path = os.path.join(self.current_dir_path, "feeds")
        self.__empty_database_file_path = os.path.join(
            self.feed_folder_path, "empty.sqlite3")

        # ścieżki do folderów ze slabościami CWE - niezbędne do karmienia aplikacji
        self.__all_cwe_details_dir = os.path.join(
            self.feed_folder_path, "cwe_details")
        self.__all_cwe_ids_dir = os.path.join(self.feed_folder_path, "cwe_ids")
        self.__all_cwe_ids_file_path = os.path.join(
            self.all_cwe_ids_dir, "cwe_all.json")
        self.__all_cwe_ids_list = self.get_all_cwe_ids()

        # ścieżki do folderów z podatnościami CVE - niezbędne do karmienia aplikacji
        self.__cve_details_dir = os.path.join(
            self.feed_folder_path, "cve_details")
        self.__cve_ids_dir = os.path.join(self.feed_folder_path, "cve_ids")
        self.__cve_ids_file = os.path.join(self.feed_folder_path, "cve_ids")

        # ścieżki do frontendu aplikacji - niezbędne do budowania projektu
        self.__frontend_dir = os.path.join(self.current_dir_path, "frontend")

        # ścieżki do backendu aplikacji - potrzebne podczas budowania projektu
        self.__backend_dir = os.path.join(self.current_dir_path, "backend")
        self.__manage_py_path = str(
            os.path.join(self.backend_dir, "manage.py"))
        self.__backend_backend_dir = os.path.join(self.backend_dir, "backend")

        # ścieżki do requirements
        self.__requirements_file = self.get_requirements_file_path()

    @staticmethod
    def run_command(command, verbose=True):
        # Never use os.popen, always use subprocess!
        print("command: ", command)
        response = subprocess.run(str(command), shell=True)
        if response.returncode:
            raise SarenkaBuildError(f"Error while executing command {command}")

    def get_all_cwe_ids(self):
        """Zwraca listę wszystkich id słabości oprogramowania z dodatkowym id niesitniejącego CWE.
        Dane są potrzebne do stworzenia baz danych dla aplikacji api_searcher."""
        with open(self.all_cwe_ids_file_path) as json_file:
            data = json.load(json_file)
        all_cwe_ids = [cwe["cwe_id"] for cwe in data["cwe_all"]]
        all_cwe_ids.sort()
        return all_cwe_ids  # zwraca wszystkie CWE ids

    def get_requirements_file_path(self):
        if IS_WINDOWS:
            return os.path.join(self.current_dir_path, "requirements_windows.txt")
        if IS_LINUX:
            return os.path.join(self.current_dir_path, "requirements_linux.txt")
        else:
            print("You are trying to build SARENKA on not tested Operating System.")
            user_input = input(
                "Do you really want to build app like on Linux OS (y/n): ")
            if user_input == "y":
                return os.path.join(self.current_dir_path, "requirements_linux.txt")
            else:
                print("Building application canceled by user.")

    @property
    def requirements(self):
        return self.__requirements_file

    @property
    def all_cwe_ids_list(self):
        """Zwraca listę identyfikatorów wszystkich słabości CWE"""
        return self.__all_cwe_ids_list

    @property
    def cwe_dbs_name_list(self):
        # TODO dac lambdę
        return [cwe.replace("-", "_").lower() for cwe in self.__all_cwe_ids_list]

    @property
    def current_dir_path(self):
        """Zwraca ścieżkę do aktulnego folderu gdzie znajduje się całe źródło aplikacji."""
        return self.__current_dir_path

    @property
    def feed_folder_path(self):
        """Zwraca ścieżkę do folderu ogólnego gdzie znajdują się pliki z feedami dla aplikacji."""
        return self.__feed_folder_path

    @property
    def empty_database_file_path(self):
        return self.__empty_database_file_path

    # ścieżki do folderów ze slabościami CWE - niezbędne do karmienia baz aplikacji
    @property
    def all_cwe_details_dir(self):
        return self.__all_cwe_details_dir

    @property
    def all_cwe_ids_dir(self):
        return self.__all_cwe_ids_dir

    @property
    def all_cwe_ids_file_path(self):
        return self.__all_cwe_ids_file_path

    # ścieżki do folderów z podatnościami CVE - niezbędne do karmienia aplikacji
    @property
    def cve_details_dir(self):
        """Zwraca ścieżkę do plików gdzie znajdują się pliki ze szczegółowymi informajami o podatnościach CVE."""
        return self.__cve_details_dir

    @property
    def cve_ids_dir(self):
        """Zwraca ścieżkę do folderu gdzie znajduje się pliki z ogólynmi informacja o podatnosciach CVE."""
        return self.__cve_ids_dir

    @property
    def cve_ids_file(self):
        """Zwrca ścieżkę do pliku z idkami i datami podatności CVE."""
        return self.__cve_ids_file

    # ściezki do frontu aplikacji
    @property
    def frontend_dir(self):
        """Zwraca ścieżkę do folderu gdzie znajduje się frontend aplikacji sarenka"""
        return self.__frontend_dir

    # ściezki do backendu aplikacji
    @property
    def backend_dir(self):
        """Zwraca ścieżkę do folderu gdzie znajduje się backend aplikacji sarenka"""
        return self.__backend_dir

    @property
    def manage_py(self):
        return self.__manage_py_path

    @property
    def backend_backend_dir(self):
        """Zwraca ścieżkę do folderu gdzie znajduje się backend backendu aplikacji sarenka.
        Jest to folder gdzie są settingsy i bazy danych dla wszystkich aplikacji."""
        return self.__backend_backend_dir


class SarenkaBuilder:
    """Klasa odpowiadajaca za budowanie aplikacji """
    __destination_cwe_databases_dir_name = "cwe_databases"
    __user_credentials_db_filename = "user_credentials.sqlite3"

    def __init__(self, verbose=True):
        self.is_verbose = verbose
        self.helper = SarenkaHelper()

    def heart_print(self, text):
        """Dodaje symbol serca do tekstu i wypisuje go na ekran konsoli"""
        print("❤ " + text)

    @property
    def cwe_db_dir(self):
        return os.path.join(self.helper.backend_backend_dir, SarenkaBuilder.__destination_cwe_databases_dir_name)

    @property
    def user_credentials_filename(self):
        """Zwraca ścieżkę do pliku bazy danych user_credentials.sqlite3"""
        return SarenkaBuilder.__user_credentials_db_filename

    @property
    def user_credentials_db_name(self):
        return self.user_credentials_filename.split(".")[0]

    @property
    def user_database_file_path(self):
        return os.path.join(self.helper.backend_backend_dir, SarenkaBuilder.__user_credentials_db_filename)

    def __install_requirements(self):
        """Instaluje wymagane biblioteki w zależności od systemu operacyjnego na jakim ma być uruchamiona aplikacja."""
        if IS_WINDOWS:
            if self.is_verbose:
                self.heart_print("Installing requirements for Windows")
        elif IS_LINUX:
            if self.is_verbose:
                self.heart_print("Installing requirements for Linux")
        else:
            raise SarenkaBuildError(
                "Unable to install packages from requirements.")

    def __create_cwes_databases_files(self):  # TRICKY
        """Tworzy docelowe bazy dancyh dla aplikacji api_vulnerabilities"""
        if self.is_verbose:
            self.heart_print(
                "Creating databases for Common Weakness Enumeration")

        # 1.Sprawdza czy taki folder już istnieje, jeśli tak uwuam całą jego zawartość
        if os.path.isdir(self.cwe_db_dir):
            self.heart_print("Removes folder with old databases for CWE ids")
            rmtree(self.cwe_db_dir)

        # 2. Tworzy folder dla baz danych dla podatności CWE
        os.makedirs(self.cwe_db_dir)
        if self.is_verbose:
            self.heart_print(
                f"Folder cwe database files in {self.cwe_db_dir} for 'api_vulnerabilities' application created.")

        # 3. Migruje jedną bazę danych CWE-NONE
        # 3.1  tworzy pustą bazę danych
        cwe_none_db = os.path.join(self.cwe_db_dir, "cwe_none.sqlite3")
        copy2(self.helper.empty_database_file_path, cwe_none_db)

        # 3.2 Migruje dane do bazy cwe
        command = f"python {self.helper.manage_py} migrate api_vulnerabilities --database=cwe_none"
        self.helper.run_command(command)

        # 4. Tworzenie pustych baz danych dla wszystkich CWE
        if self.is_verbose:
            self.heart_print(
                f"Creating {len(self.helper.all_cwe_ids_list)} empty databases: CWE-IDs + CWE-NONE.")

        # tworzy dokładnie 862 bazy danych TRICKY PART
        for cwe_id in self.helper.cwe_dbs_name_list:
            cwe_db_name = cwe_id + ".sqlite3"
            destination = os.path.join(self.cwe_db_dir, cwe_db_name)
            copy2(cwe_none_db, destination)

        if self.is_verbose:
            self.heart_print(
                f"{len(self.helper.all_cwe_ids_list)} empty databases for application 'api_vulnerabilities' created.")

    def __create_user_credentials_database(self):
        """Funkcja tworząca nową bazę dla danych uwierzytelniających użytkownika"""
        if self.is_verbose:
            self.heart_print("Creating database file for user credentials.")

        destination = self.user_database_file_path
        # usuwa stary plik bazy danych z danymi uwierzytelniającymi użytkownika w serwisach trzecich.
        if os.path.isfile(destination):
            self.heart_print(
                f"Removing old user credentials database file: {destination}")
            os.remove(destination)

        source = self.helper.empty_database_file_path
        copy2(source, destination)

        if self.is_verbose:
            self.heart_print(f"Empty database file {destination} created")

        if self.is_verbose:
            self.heart_print(
                "Applying migration to Common Weakness Enumeration databases")

        command = f"python {self.helper.manage_py} migrate api_searcher --database={self.user_credentials_db_name}"
        self.helper.run_command(command, verbose=self.is_verbose)

        if self.is_verbose:
            print(
                f"Applied migrations to {self.user_credentials_db_name} database for 'api_searcher' application.")

    def __feed_cwe_databases(self):  # TODO
        if self.is_verbose:
            self.heart_print("Saving Common Weakness Enumeration to databases")
        # TODO - zapisać do bazy wszystkie CWE

        if self.is_verbose:
            self.heart_print(
                "Saving Common Vulnerabilities and Exposures to databases")
        # TODO - zapisać do bazy wszystkie CVE

    def __build_frontend(self):  # TODO
        if self.is_verbose:
            self.heart_print("Installing React Requirements ")
        subprocess.Popen("npm install", cwd=self.helper.frontend_dir, shell=True)


    def run(self):
        starting_time = perf_counter()
        # self.__install_requirements()
        # self.__create_cwes_databases_files()
        # self.__create_user_credentials_database()



        # self.__feed_cwe_databases()
        self.__build_frontend()
        performance = perf_counter() - starting_time
        self.heart_print(f"Builded in {performance} seconds.")


class SarenkaEnvCreator:
    def __init__(self):
        self.helper = SarenkaHelper()

    def __create_env_linux(self):
        """
        Funkcja pomocnicza tworząca środowisko w systemie Linux
        """
        # TODO dodac sciezki env
        current_dir_path = self.helper.current_dir_path
        self.helper.run_command("pip3 install virtualenv")
        self.helper.run_command("virtualenv sarenka_env")
        self.helper.run_command("virtualenv sarenka_env")
        self.helper.run_command("source sarenka_env/bin/activate")

    def __create_env_windows(self):
        self.helper.run_command("pip3 install virtualenv")
        self.helper.run_command("virtualenv sarenka_env")
        self.helper.run_command("virtualenv sarenka_env")
        self.helper.run_command("source sarenka_env/bin/activate")

    def run(self):
        """Uruchamia komendy tworzące środowisko w zalezności od systemu operacyjnego na którym uruchomiono skrypt."""
        if IS_LINUX:
            self.__create_env_linux()
        if IS_WINDOWS:
            self.__create_env_windows()


class SarenkaCommand:
    def __init__(self, verbose=True):
        # self.env_creator = SarenkaEnvCreator()
        self.builder = SarenkaBuilder(verbose)

    def create_env(self):
        # self.env_creator.run()
        raise NotImplementedError

    def info(self):
        raise NotImplementedError

    def build(self):
        print("Do you really want to build application? It ")
        user_input = input("Proceed (y/n): ")
        if user_input == "y":
            self.builder.run()
        else:
            print("Building application canceled by user.")


if __name__ == "__main__":
    print("!!! It is in develop mode !!!")
    sarenka_command = SarenkaCommand()
    sarenka_command.build()
