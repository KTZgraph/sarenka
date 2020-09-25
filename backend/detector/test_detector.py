import unittest
from detector import Detector

class TestDetector(unittest.TestCase):
    # TODO: zmockować plik detectora

    def test_detector_exists(self):
        detector_data = Detector("apache")
        self.assertEqual(detector_data.search_shodan, ['Server: Apache', 'Server: Apache/2.4.29[139 chars]3.9'])

    def test_detector_does_not_exists(self):
        detector_data = Detector("noexistingsoftware")


if __name__ == "__main__":
    unittest.main()