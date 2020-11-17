from unittest import TestCase
from converty.planck import(
    meters_to_lp,
    lp_to_meters
)


class TestPlanckConversions(TestCase):

    def test_meters_to_planck_lengths(self):

        self.assertAlmostEqual(meters_to_lp(1), 6.187927353732868e+34)

    def test_planck_lengths_to_meters(self):

        self.assertAlmostEqual(lp_to_meters(1), 1.616049999e-35)