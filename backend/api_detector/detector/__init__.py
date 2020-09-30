import unittest

from api_detector.detector.detector import Detector


class TestARecord(unittest.TestCase):
    # TODO: mocki i refaktor

    def test_get_ip(self):
        ip_val = ARecord.get_ip('tutorialspoint.com')
        self.assertEqual(ip_val, ['94.130.82.52'])