import unittest

from api_dns.a_record import ARecord, ARecordWrongFQDNError


class TestARecord(unittest.TestCase):
    # TODO: mocki i refaktor

    def test_get_ip(self):
        ip_val = ARecord.get_ip('tutorialspoint.com')
        self.assertEqual(ip_val, ['94.130.82.52'])

        ip_val = ARecord.get_ip('renmich.faculty.wmi.amu.edu.pl')
        self.assertEqual(ip_val, ['150.254.78.21'])

        with self.assertRaises(ARecordWrongFQDNError):
            ARecord.get_ip('https://marcing.faculty.wmi.amu.edu.pl/DSIK/cwiczenia5.html')

    def test_get_cname(self):
        cname_val = ARecord.get_cname('mail.google.com')
        self.assertIsNotNone(cname_val)

        cname_val = ARecord.get_cname('renmich.faculty.wmi.amu.edu.pl')
        self.assertIsNotNone(cname_val)

        with self.assertRaises(ARecordWrongFQDNError):
            ARecord.get_cname('https://marcing.faculty.wmi.amu.edu.pl/DSIK/cwiczenia5.html')


if __name__ == "__main__":
    unittest.main()