import unittest
from detector import detector

class TestDetector(unittest.TestCase):
    # TODO: zmockować plik detectora

    @classmethod
    def setUpClass(cls):
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    def setUp(self):
        self.detector_obj = detector.Detector("apache")

    def tearDown(self):
        pass

    def test_detector_exists(self):
        detector_data = detector.Detector("apache")
        # self.assertEqual(detector_data.search_shodan, ['Server: Apache', 'Server: Apache/2.4.29[139 chars]3.9'])

    def test_detector_does_not_exists(self):
        # self.assertRaises(detector.DetectorNotFoundError, detector.Detector, "no_existing_software")
        with self.assertRaises(detector.DetectorNotFoundError):
            detector.Detector("no_existing_software")

    def test_property(self):
        self.assertEqual(self.detector_obj.software_type, "http_server")
        self.assertEqual(self.detector_obj.favicon_url, "Not detected")
        self.assertEqual(self.detector_obj.windows_registry_path, None)



if __name__ == "__main__":
    unittest.main()