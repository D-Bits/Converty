"""
Conversions for length measurements.
"""


def feet_to_meters(feet: float) -> float:

    meters = feet / 3.2808
    if feet == 0:
        raise Exception('Cannot calculate zero value!\n')

    return round(meters, 2)


def meters_to_feet(meters: float) -> float:

    feet = meters * 3.2808
    if meters == 0:
        raise Exception('Cannot calculate zero value!\n')

    return round(feet, 2)


def miles_to_kilos(miles: float) -> float:

    kilos = miles / 0.62137
    if miles == 0:
        raise Exception('Cannot calculate zero value!\n')

    return round(kilos, 2)


def kilos_to_miles(kilos: float) -> float:

    miles = kilos * 0.62137
    if kilos == 0:
        raise Exception('Cannot calculate zero value!\n')
            
    return round(miles, 2)
