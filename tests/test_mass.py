from unittest import TestCase
from mass import(
    pounds_to_kilograms,
    kilograms_to_pounds,
    ounces_to_grams,
    grams_to_ounces
) 


class MassTests(TestCase):

    # Ensure that 1 lbs = 0.45 kgs
    def test_pounds_to_kilos(self):

        self.assertAlmostEqual(pounds_to_kilograms(1), 0.45, places=3)

    # Ensure that 1 kg equals 2.2 lbs
    def test_kilos_to_pounds(self):

        self.assertAlmostEqual(kilograms_to_pounds(1), 2.2, places=3)

    # Ensure that 1 oz equals 28.34 g
    def test_ounces_to_grams(self):

        self.assertAlmostEqual(ounces_to_grams(1), 28.34952, places=3)

    def test_grams_to_ounces(self):

        self.assertAlmostEqual(grams_to_ounces(1), 0.035274, places=3)