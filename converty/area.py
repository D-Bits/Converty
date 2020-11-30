"""
Unit coversions for areas.
"""


def acres_to_sqft(acres: float, rounding: int) -> float:

    sqft = acres * 43560
    if acres == 0:
        raise Exception('Cannot calculate zero value!\n')

    return round(sqft, rounding)


def sqft_to_acres(sqft: float, rounding: int) -> float:

    acres = sqft / 43560
    if sqft == 0:
        raise Exception('Cannot calculate zero value!\n')

    return round(acres, rounding)


def acres_to_hectares(acres: float, rounding: int) -> float:

    hectares = acres / 2.4711
    if acres == 0:
        raise Exception('Cannot calculate zero value!\n')

    return round(hectares, rounding)


def hectares_to_acres(hectares: float, rounding: int) -> float:

    acres = hectares * 2.4711
    if hectares == 0:
        raise Exception('Cannot calculate zero value!\n')

    return round(acres, rounding)
