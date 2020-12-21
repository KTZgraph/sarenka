from typing import Dict, List
from .product import Product 

class CVEParser:
    """
    Zna wartości pola jsona
    pytanie czy za bardzo nie rozdrabniam się na klaski?
    """
    @staticmethod
    def cve(data):
        return data["id"]

    @staticmethod
    def cvss_vector(data):
        return data["cvss-vector"]

    @staticmethod
    def complexity(data):
        return data["access"]["complexity"].lower()

    @staticmethod
    def authentication(data):
        return data["access"]["authentication"].lower()

    @staticmethod
    def vector(data):
        return data["access"]["vector"].lower()

    @staticmethod
    def cvss(data):
        return data["cvss"]

    @staticmethod
    def cwe(data):
        return data["cwe"]

    @staticmethod
    def title(data): #TODO struktura
        return data.get("oval")[0]["title"]

    @staticmethod
    def products(data)->List[Product]:
        """Parses 
        cpe:/<part>:<vendor>:<product>:<version>:<update>:<edition>:<language>
        <part>
        a for applications,
        h for hardware platforms, or
        o for operating systems.
        TODO: jakies reguły na OS  żeby dobrze wyciągało poprawnie"""
        data = data["vulnerable_product"]
        # print(data)


        vendor_idx = 3
        name_idx = 4
        version_idx = 5
        system_idx = 6

        products_list =[]
        for product_data in data:
            p = product_data.split(":")

            products_list.append(
                Product(
                    vendor=p[vendor_idx],
                    name= p[name_idx],
                    version=p[version_idx],
                    system= p[system_idx]
                )
            )
        
        return products_list

    @staticmethod
    def availability(data):
        return data["impact"]["availability"]

    @staticmethod
    def confidentiality(data):
        return data["impact"]["confidentiality"]

    @staticmethod
    def integrity(data):
        return data["impact"]["integrity"]

    @staticmethod
    def summary(data):
        return data["summary"]