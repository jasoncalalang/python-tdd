import unittest

def is_valid_luhn(number: str) -> bool:
    pass  # TODO: Implement this function

class TestLuhnAlgorithm(unittest.TestCase):
    
    def test_valid_luhn(self):
        self.assertTrue(is_valid_luhn('79927398713'))

    def test_invalid_luhn(self):
        self.assertFalse(is_valid_luhn('79927398712'))

    def test_valid_credit_card(self):
        self.assertTrue(is_valid_luhn('4532015112830366'))

    def test_invalid_credit_card(self):
        self.assertFalse(is_valid_luhn('1234567812345670'))

    def test_non_numeric_string(self):
        with self.assertRaises(ValueError):
            is_valid_luhn('invalid')

if __name__ == '__main__':
    unittest.main()
