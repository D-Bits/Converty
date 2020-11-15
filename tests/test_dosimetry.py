from unittest import TestCase
from dosimetry import(
    rems_to_sieverts, 
    sieverts_to_rems,
    rads_to_grays,
    grays_to_rads
) 


class DosimetryTests(TestCase):

    # Test that 1 rem equals 0.01 Sv
    def test_rems_to_sieverts(self):

        self.assertAlmostEqual(rems_to_sieverts(1), 0.01)

    # Test that 1 Sv equals 100 rems
    def test_sieverts_to_rems(self):

        self.assertAlmostEqual(sieverts_to_rems(1), 100)

    def test_rads_to_grays(self):

        self.assertAlmostEqual(rads_to_grays(1), 0.01)

    def test_grays_to_rads(self):

        self.assertAlmostEqual(grays_to_rads(1), 100)