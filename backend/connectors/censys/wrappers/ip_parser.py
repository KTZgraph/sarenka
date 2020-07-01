from common.dict_x import DictX
from .dns_wrapper import DNSWrapper
# from dns_wrapper import DNSWrapper
from .https_wrapper import HTTPSWrapper
# from https_wrapper import HTTPSWrapper

class IPParser:
    # TODO zabezpieczenia na brak danych 
    """
    Zna strukturę odpowiedzi od censysa dla zapytań dotyczących adresu ip
    https://censys.io/ipv4/8.8.8.8
    
    """
    def __init__(self, data):
        self.data = DictX(data)

    def get_ports(self):
        """
        Osobno z pierwszego zagnieżdzęnia wyciągam porty
        - moze być przydatne w porównywaniu z self.get_protocols()
        """
        ports = []
        for key in list(self.data.keys()):
            if key.isnumeric():
                ports.append(key)
        return ports


    # ---- protokoły ----
    def get_dns(self):
        """
        Bo różne usługi nie musza być na standardowych portach
        """
        ports = self.get_ports()
        for port in ports:
            data_dns = self.data[port].get("dns")

            if data_dns:
                return DNSWrapper(data_dns)

    def get_https(self):
        """
        Bo różne usługi nie musza być na standardowych portach
        """
        ports = self.get_ports()
        for port in ports:
            data_https = self.data[port].get("https")

            if data_https:
                return HTTPSWrapper(data_https).to_json

    def get_os(self):
        """
        W metadata są os i os_description
        """
        response = None
        metadata = self.data.get("metadata")
        if metadata:
            os = metadata.get("os")
            os_description = metadata.get("os_description")
            response = list(set([os, os_description]))
        
        return response

    def get_protocols(self):
        """
        Ten sam protokół moze być wykorzystywany używany na kilku portach
        """
        protocols = self.data.get("protocols")
        protocols_port = {}
        used_protocols = []
        for protocol in protocols:
            port, protocol_name = protocol.split("/")
            if protocol_name in protocols_port:
                protocols_port[protocol_name].append(port)
            else:
                protocols_port.update({protocol_name: [port]})
                used_protocols.append(protocol_name)

        return protocols_port, used_protocols
    
    def get_location(self):
        """
        Jeśli zmieni się struktura odpowiedzi to tutaj tylko zmieniać
        """
        location = DictX(self.data.get("location"))
        if location:
            response = {}
            response.update({"country" : location.country})
            response.update({"longitude" : location.longitude})
            response.update({"latitude" : location.latitude})
            response.update({"timezone" : location.timezone})
            response.update({"continent" : location.continent})
            response.update({"registered_country" : {location.registered_country_code : location.registered_country}})
        
            return DictX(response)

    def get_autonomous_system(self):
        """
        Jeśli zmieni się struktura odpowiedzi to tutaj tylko zmieniać
        autonomous_system": {"description": "GOOGLE", "rir": "unknown", "routed_prefix": "8.8.8.0/24", "country_code": "US", "path": [15169], "asn": 15169, "name": "GOOGLE"}, 
        """
        autonomous_system = DictX(self.data.get("autonomous_system"))
        if autonomous_system:
            response = {}
            response.update({"description" : autonomous_system.description})
            response.update({"rir" : autonomous_system.rir})
            response.update({"routed_prefix" : autonomous_system.routed_prefix})
            response.update({"path" : autonomous_system.path})
            response.update({"asn" : autonomous_system.asn})
            response.update({"name" : autonomous_system.name})

            return DictX(response)
    
    @property
    def updated_at(self):
        return self.data.get("updated_at") if self.data.get("updated_at") else None

