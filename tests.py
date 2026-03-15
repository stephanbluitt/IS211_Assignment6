# tests.py
import unittest
import conversions

class TestConversions(unittest.TestCase):

    def test_convertCelsiusToKelvin(self):
        cases = [
            (300.0, 573.15), 
            (0.0, 273.15), 
            (-273.15, 0.0), 
            (100.0, 373.15), 
            (37.0, 310.15)
        ]
        for celsius, expected in cases:
            print(f"Testing: {celsius} C should be {expected} K")
            result = conversions.convertCelsiusToKelvin(celsius)
            self.assertEqual(result, expected)

    def test_convertCelsiusToFahrenheit(self):
        cases = [
            (300.0, 572.0), 
            (0.0, 32.0), 
            (-40.0, -40.0), 
            (100.0, 212.0), 
            (37.0, 98.6)
        ]
        for celsius, expected in cases:
            print(f"Testing: {celsius} C should be {expected} F")
            result = conversions.convertCelsiusToFahrenheit(celsius)
            self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
