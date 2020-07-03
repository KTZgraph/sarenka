from typing import Dict, Tuple, Sequence, List, NoReturn
import subprocess


class Hardware:
    @staticmethod
    def get_bios()->Dict:
        """
        Returns Bios version
        """
        value =  subprocess.getoutput("wmic bios get smbiosbiosversion")
        response =  {
            "name" : value.split()[0],
            "version": value.split()[1]
        }
        return response

    @staticmethod
    def get_commputer_name()->Dict:
        """
        Returns name name_computer
        """
        name_computer =  subprocess.getoutput("wmic computersystem get name,systemtype")
        response =  {
            "name" : name_computer.split()[2],
            "system_type": name_computer.split()[3]
        }
        return response
    
    @staticmethod
    def get_another_command()->Dict:
        """
        Tutaj sobie implementujesz kolejne metody
        """
        pass

    @staticmethod
    def to_json()->Dict:
        response = {}
        response.update({"bios": Hardware.get_bios()})
        response.update({"computer_name": Hardware.get_commputer_name()})

        # response.update({"moja nazwa klucza": Hardware.get_another_command()})
        return response  