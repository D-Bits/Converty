from unittest import TestCase
from area import(
    acres_to_sqft,
    sqft_to_acres,
    acres_to_hectares,
    hectares_to_acres
)


# Unit tests for area conversions
class AreaTests(TestCase):

    # Test that 1 ac = 43,560 sq. ft.
    def test_acres_to_sqft(self):

        self.assertAlmostEqual(acres_to_sqft(1), 43560)
        
    # Test that 43,560 sq. ft. = 1 ac
    def test_sqft_to_acres(self):

        self.assertAlmostEqual(sqft_to_acres(43560), 1)

    # Test that 1 ac = 0.4 ha
    def test_acres_to_hectares(self):

        self.assertAlmostEqual(acres_to_hectares(1), 0.4)

    # Test that 1 ha = 2.47 ac
    def test_hectares_to_acres(self):

        self.assertAlmostEqual(hectares_to_acres(1), 2.47)