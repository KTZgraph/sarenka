from typing import Dict
import subprocess


class Hardware:
    @staticmethod
    def get_bios() -> Dict:
        """
        Returns Bios version
        """
        value = subprocess.getoutput("wmic bios get smbiosbiosversion")
        response = {
            "name": value.split()[0],
            "version": value.split()[1]
        }
        return response

    @staticmethod
    def get_commputer_name() -> Dict:
        """
        Returns name name_computer
        """
        name_computer = subprocess.getoutput("wmic computersystem get name,systemtype")

        response = {
            "name": name_computer.split()[2],
            "system_type": name_computer.split()[3]
        }
        return response

    @staticmethod
    def get_commputer_information() -> Dict:
        """
        Returns name commputer_information
        """
        commputer_serial_number = subprocess.getoutput("wmic bios get serialnumber")
        total_physical_memory = subprocess.getoutput("wmic COMPUTERSYSTEM get TotalPhysicalMemory")
        mac_address = subprocess.getoutput("wmic nic get macaddress")
        computer_manufacturer = subprocess.getoutput("WMIC COMPUTERSYSTEM GET MANUFACTURER")

        response = {
            "commputer_serial_number": commputer_serial_number.split()[1],
            "total_physical_memory": total_physical_memory.split()[1],
            "mac_address???": mac_address.split()[1],
            "computer_manufacturer": ' '.join(computer_manufacturer.split()[1:]),

        }
        return response

    @staticmethod
    def get_baseboard_information() -> Dict:
        """
        Returns name baseboard_information
        """
        product = subprocess.getoutput("wmic baseboard get product")
        manufacturer = subprocess.getoutput("wmic baseboard get manufacturer")
        version = subprocess.getoutput("wmic baseboard get version")
        serialnumber = subprocess.getoutput("wmic baseboard get serialnumber")

        response = {
            "product": product.split()[1],
            "manufacturer": ' '.join(manufacturer.split()[1:]),
            "version": version.split()[1],
            "serialnumber": serialnumber.split()[1],

        }
        return response

    @staticmethod
    def get_operation_system() -> Dict:
        """
        Returns name operation_system
        """
        os_architecture = subprocess.getoutput("wmic OS get OSArchitecture")
        other_information = subprocess.getoutput('systeminfo | findstr /C:"OS"')
        other_information = dict(
            map(str.strip, sub.split(':', 1)) for sub in other_information.split('\n') if ':' in sub)
        response = {
            "name": other_information["OS Name"],
            "version": other_information["OS Version"],

            "manufacturer": other_information["OS Manufacturer"],
            "configuration": other_information["OS Configuration"],
            "build_type": other_information["OS Build Type"],

            "os_architecture": os_architecture.split()[1],

        }

        return response

    @staticmethod
    def get_another_command() -> Dict:
        """
        Tutaj sobie implementujesz kolejne metody
        """
        pass

    @staticmethod
    def to_json() -> Dict:
        response = {}
        response.update({"bios": Hardware.get_bios()})
        response.update({"computer_name": Hardware.get_commputer_name()})
        response.update({"commputer_information": Hardware.get_commputer_information()})
        response.update({"operation_system": Hardware.get_operation_system()})
        response.update({"baseboard_information": Hardware.get_baseboard_information()})

        # response.update({"moja nazwa klucza": Hardware.get_another_command()})
        return response