"""
Conversions for Planck units to metric units.
"""


def meters_to_planck_lengths(meters): 

    conversion = 1.61605 * 10**-35
    planck_lengths = meters / conversion
    if meters == 0:
        raise Exception('Cannot calculate zero value!\n')

    return round(planck_lengths, 2)


def planck_lengths_to_meters(pl):

    conversion = 1.61605 * 10**-35
    meters = pl * conversion
    if pl == 0:
        raise Exception('Cannot calculate zero value!\n')

    return meters

