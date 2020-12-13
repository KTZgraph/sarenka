import socket
import ipaddress
from pyroute2 import IPRoute


class LocalNetworkData:
    """Klasa zwracajaca informacje o lokalnej sieci."""
    def __init__(self):
        self.__ip_adress = socket.gethostbyname(socket.gethostname())
        self.__network = ipaddress.IPv4Network(self.__ip_adress)
        self.__netmask = ipaddress.IPv4Network(self.__ip_adress).netmask
        self.__intefaces = self.get_local_network_interfaces()

    @property
    def ip_address(self):
        return self.__ip_adress

    @property
    def network(self):
        return self.__network

    @property
    def netmask(self):
        return self.__netmask

    @property
    def intefaces(self):
        return self.__intefaces

    @property
    def values(self):
        return {
            "ip_address": str(self.ip_address),
            "network": str(self.network),
            "netmask": str(self.netmask),
            "interfaces": self.intefaces
        }

    @staticmethod
    def get_local_ip_adress():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]

    @staticmethod
    def get_local_netmask():
        """
        192.168.0.36
        192.168.0.36/32
        255.255.255.255
        """
        ip_addr = socket.gethostbyname(socket.gethostname())
        network_adress = ipaddress.IPv4Network(ip_addr)
        netmask = ipaddress.IPv4Network(ip_addr).netmask
        return ip_addr, network_adress, netmask

    @staticmethod
    def get_local_network_interfaces():
        """
        [{'iface': 11, 'addr': '192.168.0.36', 'mask': 24}]
        :return:
        """
        ip = IPRoute()
        # print([x.get_attr('IFLA_IFNAME') for x in ip.get_links()])
        info = [{'iface': x['index'], 'addr': x.get_attr('IFA_ADDRESS'), 'mask': x['prefixlen']} for x in ip.get_addr()]

        return {"iface": [i['iface'] for i in info]}

