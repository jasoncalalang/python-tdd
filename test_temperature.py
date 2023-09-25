# test_temperature.py
import unittest
import temperature  # assuming the implementation will be in a 'temperature.py' file inside 'src' directory

class TestTemperatureConversion(unittest.TestCase):
    def test_fahrenheit_to_celsius(self):
        self.assertEqual(temperature.fahrenheit_to_celsius(32), 0)
        self.assertEqual(temperature.fahrenheit_to_celsius(212), 100)

if __name__ == '__main__':
    unittest.main()
