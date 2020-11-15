from unittest import TestCase
from lengths import(
    feet_to_meters,
    meters_to_feet,
    miles_to_kilos,
    kilos_to_miles
)

# Length unit tests
class LengthTests(TestCase):

    # Test that 1ft = 0.3m
    def test_feet_to_meters(self):

        self.assertAlmostEqual(feet_to_meters(1), 0.3)

    # Test that 1 m = 3.28 ft.
    def test_meters_to_feet(self):

        self.assertAlmostEqual(meters_to_feet(1), 3.28)

    # Test that 1 mi = 1.61 km (rounded)
    def test_miles_to_kilos(self):

        self.assertAlmostEqual(miles_to_kilos(1), 1.61)

    # Test that 1 km = 0.62 mi
    def test_kilos_to_miles(self):

        self.assertAlmostEqual(kilos_to_miles(1), 0.62)    