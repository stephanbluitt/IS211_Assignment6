# tests.py
import unittest
import conversions

class TestCelsiusConversions(unittest.TestCase):

    def test_convertCelsiusToKelvin(self):
        """Tests the conversion from Celsius to Kelvin."""
        cases = [
            (300.0, 573.15),
            (0.0, 273.15),
            (-273.15, 0.0),
            (100.0, 373.15),
            (-40.0, 233.15)
        ]
        
        for celsius, expected in cases:
            with self.subTest(celsius=celsius, expected=expected):
                # The assignment requires a printed message for every test case
                print(f"Testing CelsiusToKelvin: {celsius}°C -> {expected}K")
                result = conversions.convertCelsiusToKelvin(celsius)
                self.assertAlmostEqual(result, expected, places=2)

    def test_convertCelsiusToFahrenheit(self):
        """Tests the conversion from Celsius to Fahrenheit."""
        cases = [
            (300.0, 572.0),
            (0.0, 32.0),
            (-40.0, -40.0),
            (100.0, 212.0),
            (37.0, 98.6)
        ]
        
        for celsius, expected in cases:
            with self.subTest(celsius=celsius, expected=expected):
                print(f"Testing CelsiusToFahrenheit: {celsius}°C -> {expected}°F")
                result = conversions.convertCelsiusToFahrenheit(celsius)
                self.assertAlmostEqual(result, expected, places=2)

if __name__ == '__main__':
    # verbosity=2 provides more detailed output in the terminal
    unittest.main(verbosity=2)
