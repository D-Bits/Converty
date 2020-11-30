""" 
A collection of functions to do conversions for 
measurements of ionizing radiation (Rems, Sieverts, etc)
"""


def rems_to_sieverts(rems: float) -> float:

    sieverts = rems / 100
    if rems == 0:
        raise Exception('Cannot calculate zero value!\n')

    return round(sieverts, 2)


def sieverts_to_rems(sieverts: float) -> float:

    rems = sieverts * 100
    if sieverts == 0:
        raise Exception('Cannot calculate zero value!\n')

    return round(rems, 2)


def rads_to_grays(rads: float) -> float:

    grays = rads /100
    if rads == 0:
        raise Exception('Cannot calculate zero value!\n')

    return round(grays, 2) 
    

def grays_to_rads(grays: float) -> float:

    rads = grays * 100
    if grays == 0:
        raise Exception('Cannot calculate zero value!\n')
    return round(rads, 2)
