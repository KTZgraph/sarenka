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
    def title(data):
        return data["oval"][0]["title"]

    @staticmethod
    def products(data):
        """Parses 
        cpe:/<part>:<vendor>:<product>:<version>:<update>:<edition>:<language>
        <part>
        a for applications,
        h for hardware platforms, or
        o for operating systems.
        TODO: jakies reguły na OS  żeby dobrze wyciągało poprawnie"""
        data = data["vulnerable_product"]
        print(data)


        vendor_idx = 3
        prodyct_idx = 4
        version_idx = 5
        system_idx = 6

        products_list =[]
        for product in data:
            print(product)
            p = product.split(":")

            tmp_dict={
                "vendor": p[vendor_idx],
                "product": p[prodyct_idx],
                "vesion": p[version_idx],
                "system": p[system_idx]
            }
            
            products_list.append(tmp_dict)
        
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