from unittest import TestCase
from temperature import(
    fahrenheit_to_celsius,
    celsius_to_fahrenheit,
    celsius_to_kelvin,
    kelvin_to_celsius,
    fahrenheit_to_kelvin,
    kelvin_to_fahrenheit
)


# Temperature unit tests
class TempTests(TestCase):

    # Test that 1 degree fahrenheit = -17.22 degrees celsius
    def test_fahrenheit_to_celsius(self):

        self.assertAlmostEqual(fahrenheit_to_celsius(1), -17.22)

    # Test that 1 degree C = 33.8 degress F
    def test_celsius_to_fahrenheit(self):

        self.assertAlmostEqual(celsius_to_fahrenheit(1), 33.8)

    # Tst that 1 degree C = 274.15 degrees K
    def test_celsius_to_kelvin(self):

        self.assertAlmostEqual(celsius_to_kelvin(1), 274.15)

    # Test that 1 degree K = -272.15 C
    def test_kelvin_to_celsius(self):

        self.assertAlmostEqual(kelvin_to_celsius(1), -272.15)

    # Test that absolute zero = -273.15 Celsius
    def test_absolute_zero_celsius(self):

        self.assertAlmostEqual(kelvin_to_celsius(0), -273.15)

    # Test that 1 degree fahrenheit = 255.93 (rounded) degrees Kelvin
    def test_fahrenheit_to_kelvin(self):

        self.assertAlmostEqual(fahrenheit_to_kelvin(1), 255.93)

    # Test that 1 degree K = -457.87 degrees F
    def test_kelvin_to_fahrenheit(self):

        self.assertAlmostEqual(kelvin_to_fahrenheit(1), -457.87)

    # Test that absoulte zero in F is equal to -459.67 degrees
    def test_absolute_zero_fahrenheit(self):

        self.assertAlmostEqual(kelvin_to_fahrenheit(0), -459.67)