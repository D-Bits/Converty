"""
Unit coversions for areas.
"""


def acres_to_sqft(acres: float) -> float:


    sqft = acres * 43560
    if acres == 0:
        raise Exception('Cannot calculate zero value!\n')

    return round(sqft, 2)


def sqft_to_acres(sqft: float) -> float:

    acres = sqft / 43560
    if sqft == 0:
        raise Exception('Cannot calculate zero value!\n')

    return round(acres, 2)


def acres_to_hectares(acres: float) -> float:

    hectares = acres / 2.4711
    if acres == 0:
        raise Exception('Cannot calculate zero value!\n')

    return round(hectares, 2)


def hectares_to_acres(hectares: float) -> float:

    acres = hectares * 2.4711
    if hectares == 0:
        raise Exception('Cannot calculate zero value!\n')

    return round(acres, 2)
