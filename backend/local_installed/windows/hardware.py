from typing import Dict, Tuple, Sequence, List, NoReturn
import subprocess


class Hardware:
    def __init__(self):
        pass
    def get_bios(self)->str:
        """
        Returns Bios version
        """
        value =  subprocess.getoutput("wmic bios get smbiosbiosversion")
        print(value)
        response =  {
            "name" : value.split()[0],
            "version": value.split()[1]
        }
        return response
    
    def get_another_command(self)->str:
        """
        Tutaj sobie implementujesz kolejne metody
        """
        pass

    def to_json(self)->Dict:
        response = {}
        response.update({"bios": self.get_bios()})
        # response.update({"moja nazwa klucza": self.get_another_command()})
        return response  