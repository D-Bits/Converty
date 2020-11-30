"""
Conversions for length measurements.
"""


def feet_to_meters(feet: float, rounding: int) -> float:

    meters = feet / 3.2808
    if feet == 0:
        raise Exception('Cannot calculate zero value!\n')

    return round(meters, rounding)


def meters_to_feet(meters: float, rounding: int) -> float:

    feet = meters * 3.2808
    if meters == 0:
        raise Exception('Cannot calculate zero value!\n')

    return round(feet, rounding)


def miles_to_kilos(miles: float, rounding: int) -> float:

    kilos = miles / 0.62137
    if miles == 0:
        raise Exception('Cannot calculate zero value!\n')

    return round(kilos, rounding)


def kilos_to_miles(kilos: float, rounding: int) -> float:

    miles = kilos * 0.62137
    if kilos == 0:
        raise Exception('Cannot calculate zero value!\n')
            
    return round(miles, rounding)
