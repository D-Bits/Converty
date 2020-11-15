from unittest import TestCase
from planck_units import(
    meters_to_planck_lengths,
    planck_lengths_to_meters
)


class TestPlanckConversions(TestCase):

    def test_meters_to_planck_lengths(self):

        self.assertAlmostEqual(meters_to_planck_lengths(1), 6.187927353732868e+34)

    def test_planck_lengths_to_meters(self):

        self.assertAlmostEqual(planck_lengths_to_meters(1), 1.616049999e-35)