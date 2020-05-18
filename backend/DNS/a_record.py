import dns.resolver

class ARecord:
    """
    pip install git+https://github.com/rthalley/dnspython
    nazwa biblioteki i importu są inne -,- 
    dlatego mogą być problemy z importmai xD
    https://www.tutorialspoint.com/python_network_programming/python_dns_look_up.htm
    """
    def __init__(self):
        pass


if __name__ == "__main__":
    result = dns.resolver.query('tutorialspoint.com', 'A')
    for ipval in result:
        print('IP', ipval.to_text())

    result = dns.resolver.query('mail.google.com', 'CNAME')
    for cnameval in result:
        print (' cname target address:', cnameval.target)