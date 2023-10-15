import unittest

def prime_factors(n):
    factors = []
    divisor = 2
    
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1

    return factors

class TestPrimeFactors(unittest.TestCase):
    
    def test_prime_factors_of_1(self):
        self.assertEqual(prime_factors(1), [])

    def test_prime_factors_of_2(self):
        self.assertEqual(prime_factors(2), [2])

    def test_prime_factors_of_3(self):
        self.assertEqual(prime_factors(3), [3])

    def test_prime_factors_of_4(self):
        self.assertEqual(prime_factors(4), [2, 2])

    def test_prime_factors_of_6(self):
        self.assertEqual(prime_factors(6), [2, 3])

    def test_prime_factors_of_9(self):
        self.assertEqual(prime_factors(9), [3, 3])

    def test_prime_factors_of_12(self):
        self.assertEqual(prime_factors(12), [2, 2, 3])

if __name__ == '__main__':
    unittest.main()
