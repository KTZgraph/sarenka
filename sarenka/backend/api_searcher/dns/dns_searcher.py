"""
Pobiera dane o rekordach DNS - wysztkie sotępne w bibliotece:
A
NS
MD
MF
CNAME
SOA
MB
MG
MR
NULL
WKS
PTR
HINFO
MINFO
MX
TXT
RP
AFSDB
X25
ISDN
RT
NSAP
NSAP_PTR
SIG
KEY
PX
GPOS
AAAA
LOC
NXT
SRV
NAPTR
KX
CERT
A6
DNAME
OPT
APL
DS
SSHFP
IPSECKEY
RRSIG
NSEC
DNSKEY
DHCID
NSEC3
NSEC3PARAM
TLSA
HIP
NINFO
CDS
CDNSKEY
OPENPGPKEY
CSYNC
SPF
UNSPEC
EUI48
EUI64
TKEY
TSIG
IXFR
AXFR
MAILB
MAILA
ANY
URI
CAA
AVC
AMTRELAY
TA
DLV
"""
from typing import List, Dict
import dns.resolver
import dns.exception
import dns.reversename
from dns.rdatatype import RdataType
import ipaddress
import socket


class DNSSearcherError(Exception):
    """
    Zgłasza wyjątki gdy nie można pobrć danych o rekordach DNS.
    """
    # https://catonmat.net/asynchronous-dns-resolution warto zobacyzc
    def __init__(self, message=None, errors=None):
        super().__init__(message)
        self.errors= errors


class DNSSearcher:
    """
    Klasa odpowiedzialna za wyszukiwanie informacji o rekordach DNS.
    """

    def __init__(self, host:str):
        try:
            socket.gethostbyname(host)
        except socket.gaierror as ex:
            raise DNSSearcherError(f"Unable to find host {host}")

        # zdecydowanie lepiej suzka dla nazw domenowych typu google.com niż 8.8.8.8
        self.host = DNSSearcher.change_to_domain_addres(host)
        # DNS host:  python.org dla http://127.0.0.1:8000/api/dns/python.org po pingu http://45.55.99.72/
        # 72.99.55.45.in-addr.arpa. dla http://127.0.0.1:8000/api/search/python.org


    @staticmethod
    def is_ipv4(host:str)->bool:
        """
        Metoda pomocnicza sprawdzająca czy podany host to adres ip czy domenowy.
        :param host: adres ip lub nazwa domenowa hosta
        :return: True jeśli argument host to adres ip, w przeciwnym wypadku zwraca False
        """
        try:
            ipaddress.IPv4Network(host)
            return True
        except ValueError:
            return False

    @staticmethod
    def change_to_domain_addres(host:str):
        """Metoda pomocnicza zwraca adres ip w postaci reverse-map nazwy domenowej.
        :param host: adres ip lub nazwa domenowa hosta
        :return: reverse-map nazwa domenowa adresu hosta
        """
        if DNSSearcher.is_ipv4(host):
            try:
                # nie wszystkie serwisy idzie z ip na domenę zamineić
                #np. python.org -> 45.55.99.72 tak ale w drugą stronę już nie
                # zdecydowanie lepiej szuka po nazwach domenowych
                host_name = socket.gethostbyaddr(host)[0] # => (hostname, alias-list, IP)
                return dns.reversename.from_address(host_name)
            except socket.herror:
                 raise DNSSearcherError(f"Unable to resolve host name from ip address= {host}")
            #
        return host

    @staticmethod
    def all_records()->List:
        """
        Atrybut klasy zwracający informacje wybranych rekordów DNS w postaci listy.
        """
        return [str(i).split(".")[1] for i in RdataType]

    def get_data(self)->List:
        result = []
        for qtype in DNSSearcher.all_records():
            try:
                answers = dns.resolver.resolve(self.host, qtype, raise_on_no_answer=False)
                if answers and answers.rrset:
                    # jak znaleziono dane
                    result.append({
                        qtype:{
                            "answers": [answer.__str__() for answer in answers],
                            "answers_rrset": answers.rrset.__str__()
                        }
                    })

            except dns.exception.DNSException:
                result.append({qtype: "Unable to detect.", "answers_rrset": "Unable to detect"})

        return result

