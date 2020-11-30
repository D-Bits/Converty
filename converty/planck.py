"""
Conversions for Planck units to metric units.
"""


# Convert meters to planck lengths
def meters_to_lp(meters: float) -> float: 

    try:
        conversion = 1.61605 * 10**-35
        planck_lengths = meters / conversion

        return round(planck_lengths, 2)

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except TypeError:
        return "Error: Must pass in an int, or a float."
        

# Convert planck lengths to meters
def lp_to_meters(lp: float) -> float:

    conversion = 1.61605 * 10**-35
    meters = lp * conversion
    if lp == 0:
        raise Exception('Cannot calculate zero value!\n')

    return round(meters, round)
