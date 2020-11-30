"""
Conversions for Planck units to metric units.
"""


# Convert meters to planck lengths
def meters_to_lp(meters: float, rounding: int) -> float: 

    conversion = 1.61605 * 10**-35
    if meters == 0:
        raise Exception('Cannot calculate zero value!\n')
    planck_lengths = meters / conversion

    return round(planck_lengths, rounding)


# Convert planck lengths to meters
def lp_to_meters(lp: float, rounding: int) -> float:

    conversion = 1.61605 * 10**-35
    meters = lp * conversion
    if lp == 0:
        raise Exception('Cannot calculate zero value!\n')

    return round(meters, rounding)
