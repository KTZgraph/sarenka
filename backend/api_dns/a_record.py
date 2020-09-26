import dns.resolver


class ARecordWrongFQDNError(Exception):
    """
    zgłasza wyjątki gdy podany dres jest nieprawidłowy
    """
    def __init__(self, message=None, errors=None):
        super().__init__(message)
        self.errors= errors

class ARecord:
    """
    pip install git+https://github.com/rthalley/dnspython
    nazwa biblioteki i importu są inne -,-
    dlatego mogą być problemy z importmai xD
    https://www.tutorialspoint.com/python_network_programming/python_dns_look_up.htm

        NAME                    TYPE   VALUE
    --------------------------------------------------
    bar.example.com.        CNAME  foo.example.com.
    foo.example.com.        A      192.0.2.23

    https://en.wikipedia.org/wiki/List_of_DNS_record_types
    """
    @staticmethod
    def get_ip(fqdn:str)->list:
        """
        FQDN - Fully Qualified Domain Name example www.wikipedia.org
        """
        try:
            result = dns.resolver.query(fqdn, 'A')
        except dns.resolver.NXDOMAIN:
            raise ARecordWrongFQDNError(f"Unable to resolve ip address for: {fqdn}")

        ip_val = [ipval.to_text() for ipval in result]
        return ip_val

    @staticmethod
    def get_cname(fqdn:str)->list:
        """
        CNAME - Canonical Name record
        """
        try:
            result = dns.resolver.query(fqdn, 'CNAME')
        except dns.resolver.NXDOMAIN:
            raise ARecordWrongFQDNError(f"Unable to resolve CNAME for: {fqdn}")

        cname_val = [cname.target for cname in result]
        return cname_val

    @staticmethod
    def get_mx(fqdn:str):
        """
        MX record
        """
        #TODO: zaimplementowac
        raise NotImplementedError("MX record")

    @staticmethod
    def get_ns(fqdn:str):
        """
        NS record
        """
        #TODO: zaimplementowac
        raise NotImplementedError("NS record")

    @staticmethod
    def get_dname(fqdn:str):
        """
        DNAME record or Delegation Name record
        """
        #TODO: zaimplementowac
        raise NotImplementedError("DNAME record or Delegation Name record")

    @staticmethod
    def get_aname(fqdn:str):
        """
        ANAME record
        """
        #TODO: zaimplementowac
        raise NotImplementedError("ANAME record")

# if __name__ == "__main__":
#     result = dns.resolver.query('tutorialspoint.com', 'A')
#     for ipval in result:
#         print('IP', ipval.to_text())
#
#     result = dns.resolver.query('mail.google.com', 'CNAME')
#     for cnameval in result:
#         print (' cname target address:', cnameval.target)