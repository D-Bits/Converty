"""
Unit conversions for mass.
"""


def pounds_to_kilograms(pounds: float) -> float:

    kilos = pounds / 2.2046
    if pounds == 0:
        raise Exception('Cannot calculate zero value!\n')

    return round(kilos, 2)


def kilograms_to_pounds(kilos: float) -> float:

    pounds = kilos * 2.2046
    if kilos == 0:
        raise Exception('Cannot calculate zero value!\n')

    return round(pounds, 2)


def ounces_to_grams(ounces: float) -> float:

    grams = (ounces / 0.035274)
    if ounces == 0:
        raise Exception('Cannot calculate zero value!\n')

    return grams


def grams_to_ounces(grams: float) -> float:

    ounces = grams * 0.035274
    if grams == 0:
        raise Exception('Cannot calculate zero value!\n')
            
    return ounces
