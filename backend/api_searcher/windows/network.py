import socket
import ipaddress
from pyroute2 import IPRoute

class NetworkCommand:
    @staticmethod
    def get_arp():
        """arp -a"""
        pass

    @staticmethod
    def nbtstat():
        """
        nbtstat -c
        nbtstat -n
        nbtstat -r

        :return:
        """
        pass

    @staticmethod
    def get_hostname():
        """
        hostname
        """
        pass

    @staticmethod
    def ipconfig_all():
        """
        ipconfig /all
        """
        pass

    @staticmethod
    def get_nslookup():
        """
        nslookup
        :return:
        """
        pass


    @staticmethod
    def get_getmac():
        """
        getmac
        :return:
        """
        pass


    @staticmethod
    def get_netstat_an():
        """
        netstat -an
        :return:
        """
        pass



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
        ip_addr = socket.gethostbyname(socket.gethostname())
        network_adress = ipaddress.IPv4Network(ip_addr)
        netmask = ipaddress.IPv4Network(ip_addr).netmask
        return ip_addr, network_adress, netmask

    @staticmethod
    def get_local_network_interfaces():
        ip = IPRoute()
        # print([x.get_attr('IFLA_IFNAME') for x in ip.get_links()])
        info = [{'iface': x['index'], 'addr': x.get_attr('IFA_ADDRESS'), 'mask': x['prefixlen']} for x in ip.get_addr()]
        return {"iface": [i['iface'] for i in info]}

