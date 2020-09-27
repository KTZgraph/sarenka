import unittest

from api_scraper.scrapers.general_scraper import GeneralScraper, GeneralScraperError


class TestARecord(unittest.TestCase):
    # TODO: mocki dla requests
    @classmethod
    def setUpClass(cls):
        cls.valid_urls = ["http://www.github.com", "http://www.yahoo.com",
                "http://www.github.com/pawlaczyk"]
        cls.invalid_urls = ["httpeeeeeee://www.google.com", "www.google.com"]

    def test_get_all_valid_urls(self):
        for u in self.valid_urls:
            gs = GeneralScraper(u)
            self.assertIsNotNone(gs.get_all())

    def test_get_all_invalid_urls(self):
        for u in self.invalid_urls:
            with self.assertRaises(GeneralScraperError):
                GeneralScraper(u)

    def test_get_title_exists(self):
        gs = GeneralScraper("http://www.github.com")
        self.assertIsNotNone(gs.get_title())
        self.assertIsInstance(gs.get_title(), str)

    def test_get_description_exists(self):
        gs = GeneralScraper("http://www.github.com")
        self.assertIsNotNone(gs.get_description())
        self.assertIsInstance(gs.get_description(), dict)

    def test_get_keywords_exists(self):
        gs = GeneralScraper("http://www.yahoo.com")
        self.assertIsNotNone(gs.get_keywords())
        self.assertIsInstance(gs.get_keywords(), str)

    def test_get_keywords_doesnt_exist(self):
        gs = GeneralScraper("http://www.github.com")
        self.assertIsNone(gs.get_keywords())

    def get_image_exists(self):
        gs = GeneralScraper("http://www.yahoo.com")
        self.assertIsNotNone(gs.get_image())
        self.assertIsInstance(gs.get_image(), str)