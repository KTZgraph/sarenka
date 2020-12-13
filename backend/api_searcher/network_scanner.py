import sys
import socket
import json
import nmap
import ipaddress
from pyroute2 import IPRoute


from scapy.all import ARP, Ether, srp
import xml.etree.ElementTree

def get_local_ip_adress():
    # 192.168.0.36
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

def get_local_netmask():
    """
    192.168.0.36
    192.168.0.36/32
    255.255.255.255
    """
    ip_addr = socket.gethostbyname(socket.gethostname())
    print(ip_addr)
    print(ipaddress.IPv4Network(ip_addr))
    netmask = ipaddress.IPv4Network(ip_addr).netmask
    print(netmask)

def get_local_network_information():
    """
    [{'iface': 11, 'addr': '192.168.0.36', 'mask': 24}]
    :return:
    """
    ip = IPRoute()
    print([x.get_attr('IFLA_IFNAME') for x in ip.get_links()])
    info = [{'iface': x['index'], 'addr': x.get_attr('IFA_ADDRESS'), 'mask':  x['prefixlen']} for x in ip.get_addr()]

    print(info)


def nmap_port_scan(ip_address):
    host = ip_address
    nmap_scanner = nmap.PortScanner()
    state="scaning"
    try:
        nmap_scanner.scan(host) # arguments= "-TS -p 1-65535 -sV -sT -A - Pn"
        porst = nmap_scanner[host]['tcp'].keys()
        result_list = []

        for port in porst:
            result={}
            state = nmap_scanner[host]['tcp'][port]['state']
            service = nmap_scanner[host]['tcp'][port]['name']
            product = nmap_scanner[host]['tcp'][port]['product']['version']
            result['port'] = port
            result['state'] = state
            result['service'] = service
            result['product'] = product

            if state == 'open':
                result_list.append(result)

        print(result_list)
        state = 'scanned'
        result = json.dumps(result_list)
        return json.dumps(result_list)
    except Exception as e:
        print("Wyjątek")
        print(type(e))
        print(e)



if __name__ == "__main__":
    # print(get_local_ip_adress())
    # get_local_netmask()
    # get_local_network_information()

    network_ip = "192.168.0.36"
    arp = ARP(pdst=network_ip)
    ethernet0 = Ether(dst="ff:ff:ff:ff:ff:ff")
    full_packet = ethernet0 / arp
    result_packet = srp(full_packet, timeout=3, verbose=0)[0]
    addresses = []
    print("Scanning for live host on the selected network")
    for sent, received in result_packet:
        addresses.append({"ip": received.psrc})
    print("Live Hosts")
    for address in addresses:
        print(address['ip'])
        ip_add = json.dumps(address)
        print("Scanning for ports and service")
        nmap_port_scan(address['ip'])
