# test_palindrome.py
import unittest
import palindrome

class TestPalindrome(unittest.TestCase):
    def test_is_palindrome(self):
        self.assertTrue(palindrome.is_palindrome("radar"))
        self.assertTrue(palindrome.is_palindrome("Racecar"))
        self.assertFalse(palindrome.is_palindrome("hello"))
        self.assertTrue(palindrome.is_palindrome("A man, a plan, a canal, Panama"))

if __name__ == '__main__':
    unittest.main()
