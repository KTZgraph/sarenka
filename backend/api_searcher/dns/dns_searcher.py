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
from nslookup import Nslookup
import socket
import pprint

class DNSSearcherFQDNError(Exception):
    """
    zgłasza wyjątki gdy podany dres jest nieprawidłowy
    """
    def __init__(self, message=None, errors=None):
        super().__init__(message)
        self.errors= errors

class DNSSearcher:
    """
    DNS wyszukiwanie informacji o rekordach domeny "A", "AAAA", "CNAME", "MX", "NS"
    """

    def __init__(self, host:str):
        self.host = DNSSearcher.change_to_domain_addres(host)

    @staticmethod
    def is_ipv4(host):
        try:
            ipaddress.IPv4Network(host)
            return True
        except ValueError:
            return False

    @staticmethod
    def change_to_domain_addres(host):
        if DNSSearcher.is_ipv4(host):
            return dns.reversename.from_address("216.58.201.142")
        return host

    @staticmethod
    def all_records():
        """
        Wyciąga wszystkie rekordy DNS domeny jakie obsługuje biblioteka dns
        :return:
        """
        return [str(i).split(".")[1] for i in RdataType]

    def get_data(self):
        result = []
        # for qtype in ["A", "AAAA", "CNAME", "MX", "NS"]:
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
                # elif answers:
                #     result.append({
                #         qtype:{
                #             "answers": [answer.__str__() for answer in answers],
                #             "answers_rrset": "Unable to detect"
                #         }
                #     })
                # else:
                #     result.append({
                #         qtype:{
                #             "answers": "Unable to detect",
                #             "answers_rrset": "Unable to detect"
                #         }
                #     })

            except dns.exception.DNSException:
                result.append({qtype: "Unable to detect.", "answers_rrset": "Unable to detect"})

        return result

    @property
    def values(self)->List[Dict]:
        print(type(self.get_data()))
        # zwrotka lepiej jak jest listą
        return {"dns_data" : self.get_data()}


if __name__ == "__main__":
    # HOST = "python.org"
    HOST = "wmi.amu.edu.pl"
    # a = DNSSearcher("216.58.201.142")
    # pprint.pprint(a.values)
    a = DNSSearcher(HOST)
    pprint.pprint(a.values)
