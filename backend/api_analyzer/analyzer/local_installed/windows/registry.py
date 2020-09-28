from winreg import ConnectRegistry, OpenKey, QueryInfoKey, QueryValueEx, EnumKey, HKEY_CLASSES_ROOT, HKEY_CURRENT_USER, HKEY_LOCAL_MACHINE, HKEY_USERS, HKEY_PERFORMANCE_DATA, HKEY_CURRENT_CONFIG, HKEY_DYN_DATA
import os
import enum

from api_analyzer.analyzer.local_installed.windows.installed_software import InstalledSoftware


ROOTS_HIVES = {
    "hkey_classes_root": HKEY_CLASSES_ROOT,
    "hkey_current_user": HKEY_CURRENT_USER,
    "hkey_local_machine": HKEY_LOCAL_MACHINE,
    "hkey_users": HKEY_USERS,
    "hkey_performance_data": HKEY_PERFORMANCE_DATA,
    "hkey_current_config": HKEY_CURRENT_CONFIG,
    "hkey_dyn_data": HKEY_DYN_DATA
}

class WindowsPath(enum.Enum):
    """
    Enum do przechowywania scieżek, z których odczytujemy lokalnie na Windze zainstalowane oprogramowania
    """
    hkey_local_machine = r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall'
    hkey_local_machine_wow6432node = r'HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall'


class WindowsRegistry:
    """
    Wybiera dane które są dostępne w rejestrze Windows
    """
    def __init__(self):
        self.__paths = [path for path in WindowsPath]

    def __parse_key(self, key):
        key = key.lower()
        parts = key.split('\\')
        root_hive_name = parts[0]
        root_hive = ROOTS_HIVES.get(root_hive_name)
        partial_key = '\\'.join(parts[1:])

        if not root_hive:
            raise Exception('root hive "{}" was not found'.format(root_hive_name))

        return partial_key, root_hive

    def __get_sub_keys(self, key):
        partial_key, root_hive = self.__parse_key(key)

        with ConnectRegistry(None, root_hive) as reg:
            with OpenKey(reg, partial_key) as key_object:
                sub_keys_count, values_count, last_modified = QueryInfoKey(key_object)
                try:
                    for i in range(sub_keys_count):
                        sub_key_name = EnumKey(key_object, i)
                        yield sub_key_name
                except WindowsError:
                    pass
    
    def __get_values(self, key, fields):
        partial_key, root_hive = self.__parse_key(key)

        with ConnectRegistry(None, root_hive) as reg:
            with OpenKey(reg, partial_key) as key_object:
                data = {}
                for field in fields:
                    try:
                        value, type = QueryValueEx(key_object, field)
                        data[field] = value
                    except WindowsError:
                        pass

                return data

    def __join_keys(self, path, *paths):
        path = path.strip('/\\')
        paths = map(lambda x: x.strip('/\\'), paths)
        paths = list(paths)
        result = os.path.join(path, *paths)
        result = result.replace('/', '\\')
        return result

    def get_software_key(self, key):
        all_key_softwares = []
        for sub_key in self.__get_sub_keys(key):
            path = self.__join_keys(key, sub_key)
            value = self.__get_values(path, ['DisplayName', 'DisplayVersion', 'InstallDate', 'InstallLocation', 'Publisher'])
            
            if value:
                software = InstalledSoftware(value)
                all_key_softwares.append(software.to_dict)

        return all_key_softwares

    def get_all_software(self):
        all_softwares = []
        paths = [path.value for path in WindowsPath]
        for path in paths:
            all_softwares.append({"key": path, "softwares": self.get_software_key(path)})

        return all_softwares


if __name__ == "__main__":
    windows_registry = WindowsRegistry()
    d = windows_registry.get_all_software()

