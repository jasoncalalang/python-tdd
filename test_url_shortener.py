import unittest
from URLShortener import URLShortener

class TestURLShortener(unittest.TestCase):
    def test_shorten_and_retrieve_url(self):
        shortener = URLShortener()
        original_url = "https://www.example.com"
        short_url = shortener.shorten(original_url)
        self.assertIsNotNone(short_url)
        self.assertEqual(shortener.retrieve(short_url), original_url)

if __name__ == '__main__':
    unittest.main()