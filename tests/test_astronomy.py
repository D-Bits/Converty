from unittest import TestCase
from astronomy import(
    kilometers_to_au,
    au_to_kilometers,
    miles_to_au,
    au_to_miles,
    kilometers_to_ly,
    ly_to_kilometers,
    miles_to_ly,
    ly_to_miles,
    parsecs_to_ly,
    ly_to_parsecs
)


# Unit tests for astronomical conversions
class AstronomyTests(TestCase):

    # Test that 1km = 0.0 AU
    def test_kilometers_to_au(self):

        self.assertAlmostEqual(kilometers_to_au(1), 0.0)

    # Test that 1 AU = 149597900 km
    def test_au_to_kilometers(self):

        self.assertEqual(au_to_kilometers(1), 149597900.0)

    # Test that 1mi = 0.0 AU
    def test_miles_to_au(self):

        self.assertAlmostEqual(miles_to_au(1), 0.0)

    # Test that 1 AU = 92955825.9 mi
    def test_au_to_miles(self):

        self.assertAlmostEqual(au_to_miles(1), 92955825.9)

    # Test that 1km = 0.0 ly
    def test_kilometers_to_ly(self):

        self.assertAlmostEqual(kilometers_to_ly(1), 0.0)

    # Test that 1 ly = 9460730000000 km
    def test_ly_to_kilometers(self):
    
        self.assertAlmostEqual(ly_to_kilometers(1), 9460730000000)

    # Test that 1mi = 0.0 ly
    def test_miles_to_ly(self):
    
        self.assertAlmostEqual(miles_to_ly(1), 0.0)

    # Test that 1 ly = 5878625000000 mi
    def test_ly_to_miles(self):

        self.assertEqual(ly_to_miles(1), 5878625000000)

    # Test that 1 pc = 3.26 ly
    def test_parsecs_to_ly(self):

        self.assertAlmostEqual(parsecs_to_ly(1), 3.26)

    # Test that 1 ly = 0.3066 pc
    def test_ly_to_parsecs(self):

        self.assertAlmostEqual(ly_to_parsecs(1), 0.30660174)