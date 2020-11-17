"""
Conversions for Planck units to metric units.
"""


# Convert meters to planck lengths
def meters_to_lp(meters): 

    conversion = 1.61605 * 10**-35
    planck_lengths = meters / conversion
    if meters == 0:
        raise Exception('Cannot calculate zero value!\n')

    return round(planck_lengths, 2)


# Convert planck lengths to meters
def lp_to_meters(lp):

    conversion = 1.61605 * 10**-35
    meters = lp * conversion
    if lp == 0:
        raise Exception('Cannot calculate zero value!\n')

    return round(meters, round)
