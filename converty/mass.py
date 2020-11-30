"""
Unit conversions for mass.
"""


def pounds_to_kilograms(pounds: float, rounding: int) -> float:

    kilos = pounds / 2.2046
    if pounds == 0:
        raise Exception('Cannot calculate zero value!\n')

    return round(kilos, rounding)


def kilograms_to_pounds(kilos: float, rounding: int) -> float:

    pounds = kilos * 2.2046
    if kilos == 0:
        raise Exception('Cannot calculate zero value!\n')

    return round(pounds, rounding)


def ounces_to_grams(ounces: float, rounding: int) -> float:

    grams = (ounces / 0.035274)
    if ounces == 0:
        raise Exception('Cannot calculate zero value!\n')

    return round(grams, rounding)


def grams_to_ounces(grams: float, rounding: int) -> float:

    ounces = grams * 0.035274
    if grams == 0:
        raise Exception('Cannot calculate zero value!\n')
            
    return round(ounces, rounding)
