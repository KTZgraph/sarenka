from common.common import Common
from ip_parser import IPParser


class IPWrapper:
    def __init__(self, filename="C:\\Users\\dp\\Desktop\\sarenka\\backend\\connectors\\censys\\50_56_73_47.json"):
        data = Common.file_to_dict(filename)
        ip_parser = IPParser(data)
        protocols_port, used_protocols = ip_parser.get_protocols()

        self.__protocols_port = protocols_port
        self.__protocols = used_protocols
        self.__ports = ip_parser.get_ports()
        self.__location = ip_parser.get_location()
        self.__autonomous_system = ip_parser.get_autonomous_system()
        self.__dns = ip_parser.get_dns()
        self.__https = ip_parser.get_https()
        self.__os = ip_parser.get_os()
        self.__updated_at = ip_parser.updated_at


    @property
    def to_json(self):
        pass

    @property
    def protocols_port(self):
        return self.__protocols_port

    @property
    def protocols(self):
        return self.__protocols

    @property
    def ports(self):
        return self.__ports

    @property
    def os(self):
        return self.__os

    @property
    def updated_at(self):
        return self.__updated_at

    # ---------------------- location ----------------------
    @property
    def location(self):
        return self.__location

    @property
    def country(self):
        return self.__location.country

    @property
    def longitude(self):
        return self.__location.longitude

    @property
    def latitude(self):
        return self.__location.latitude

    @property
    def timezone(self):
        return self.__location.timezone

    @property
    def continent(self):
        return self.__location.continent

    @property
    def registered_country(self):
        return self.location.registered_country


    # ---------------------- autonomous_system ----------------------
    @property
    def autonomous_system(self):
        return self.__autonomous_system

    @property
    def description(self):
        return self.autonomous_system.description

    @property
    def rir(self):
        """
        RIR - Regional Internet registry
        """
        return self.autonomous_system.rir

    @property
    def routed_prefix(self):
        return self.autonomous_system.routed_prefix

    @property
    def path(self):
        return self.autonomous_system.path

    @property
    def asn(self):
        """
        autonomous system number (ASN)
        """
        return self.autonomous_system.asn

    @property
    def name(self):
        return self.autonomous_system.name if self.autonomous_system else None

    # -------------------------- PROTOKOŁY --------------------------
    # -------------------------- DNS
    @property
    def dns(self):
        return self.__dns

    @property
    def dns_names(self):
        return self.dns.names if self.dns else None

    @property
    def dns_erros(self):
        if self.dns:
            errors = []
            
            if not self.dns.is_resolves_correctly:
                errors.append("resolves uncorrectly")

            if not self.dns.is_support:
                errors.append("not supported")

            if not self.dns.is_open_resolver:
                errors.append("no open resolver")

            if not self.dns.is_erros:
                errors.append(self.dns.is_erros)

            return errors
        
        return None

    # -------------------------- HTTPS
    @property
    def https(self):
        return self.__https

    @property
    def to_json(self):
        response = {}
        response.update({"protocols_port": self.protocols_port})
        response.update({"protocols_port" :self.protocols_port})
        response.update({"protocols" :self.protocols})
        response.update({"ports" :self.ports})
        response.update({"longitude" :self.longitude})
        response.update({"latitude" :self.latitude})
        response.update({"timezone" :self.timezone})
        response.update({"continent" :self.continent})
        response.update({"registered_country" :self.registered_country})
        response.update({"description" :self.description})
        response.update({"rir" :self.rir})
        response.update({"routed_prefix" :self.routed_prefix})
        response.update({"path" :self.path})
        response.update({"asn" :self.asn})
        response.update({"name" :self.name})
        response.update({"dns_names" :self.dns_names})
        response.update({"dns_erros" :self.dns_erros})
        response.update({"https" :self.https})
        response.update({"os" :self.os})
        response.update({"updated_at" :self.updated_at})
        return response

    def __str__(self):
        result = ""
        for item in self.to_json.items():
            result += str(item[0]) + ": " + str(item[1]) + "\n"

        return result



if __name__ == "__main__":
    ip_wrapper = IPWrapper()
    print(ip_wrapper)