from common.common import Common
from ip_parser import IPParser


class IPWrapper:
    def __init__(self, filename="C:\\Users\\dp\\Desktop\\sarenka\\backend\\connectors\\censys\\censys_ip.json"):
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
        return self.autonomous_system.name

    # -------------------------- PROTOKOŁY --------------------------
    # -------------------------- DNS
    @property
    def dns(self):
        return self.__dns

    @property
    def dns_names(self):
        return self.dns.names

    @property
    def dns_erros(self):
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

    # -------------------------- HTTPS
    @property
    def https(self):
        return self.__https



if __name__ == "__main__":
    ip_wrapper = IPWrapper()
    # print(ip_wrapper.protocols_port)
    # print(ip_wrapper.protocols)
    # print(ip_wrapper.ports)
    # print(ip_wrapper.location)
    # print(ip_wrapper.longitude)
    # print(ip_wrapper.latitude)
    # print(ip_wrapper.timezone)
    # print(ip_wrapper.continent)
    # print(ip_wrapper.registered_country)
    # print(ip_wrapper.description)
    # print(ip_wrapper.rir)
    # print(ip_wrapper.routed_prefix)
    # print(ip_wrapper.path)
    # print(ip_wrapper.asn)
    # print(ip_wrapper.name)

    print(ip_wrapper.dns_names)
    print(ip_wrapper.https)