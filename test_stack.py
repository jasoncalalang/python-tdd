import unittest

def is_valid_luhn(number: str) -> bool:
    if not number.isdigit():
        raise ValueError("Input must be a numeric string")
        
    digits = [int(digit) for digit in number]
    checksum = 0

    # Double every second digit from the right and add the individual digits to the checksum
    for i in range(-2, -len(digits) - 1, -2):
        double_digit = digits[i] * 2
        checksum += double_digit if double_digit < 10 else double_digit - 9

    # Add the other digits to the checksum
    checksum += sum(digits[-1::-2])

    return checksum % 10 == 0

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
