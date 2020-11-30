""" 
A collection of functions to do conversions for 
measurements of ionizing radiation (Rems, Sieverts, etc)
"""


def rems_to_sieverts(rems: float, rounding: int) -> float:

    sieverts = rems / 100
    if rems == 0:
        raise Exception('Cannot calculate zero value!\n')

    return round(sieverts, rounding)


def sieverts_to_rems(sieverts: float, rounding: int) -> float:

    rems = sieverts * 100
    if sieverts == 0:
        raise Exception('Cannot calculate zero value!\n')

    return round(rems, rounding)


def rads_to_grays(rads: float, rounding: int) -> float:

    grays = rads /100
    if rads == 0:
        raise Exception('Cannot calculate zero value!\n')

    return round(grays, rounding) 
    

def grays_to_rads(grays: float, rounding: int) -> float:

    rads = grays * 100
    if grays == 0:
        raise Exception('Cannot calculate zero value!\n')
    
    return round(rads, rounding)
