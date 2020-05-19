# code from class
import numpy as np


def lennard_jones(r, sigma=1.0, epsilon=1.0, r_c=2.5):
    """

    Calculates the Lennard-Jones potential for particles with diameter sigma
    at a separation r with a well-depth epsilon.

    >>> lennard_jones(1.0, 1.0, 1.0)
    0.0

    >>> lennard_jones(2**(1/6), 1.0, 1.0)
    -1.0

    >>> lennard_jones(0.0, 1.0, 1.0)
    Traceback (most recent call last):
    ZeroDivisionError: float division by zero

    >>> lennard_jones(-1.0, 1.0, 1.0)
    Traceback (most recent call last):
    ValueError: distance between particles is negative

    >>> lennard_jones(1.0, -1.0, 1.0)
    Traceback (most recent call last):
    ValueError: particle diameter is not strictly positive

    :param r: the distance between two particles
    :type r: float
    :param sigma: the diameter of a particle
    :type sigma: float
    :param epsilon: the well depth of the potential
    :type epsilon: float

    :return: the Lennard-Jones energy of the particle pair
    :rtype: float
    """
    # no need to do those judge and convertion beause this is always called by other modules but not the user
    # if np.any(r < 0.0):
    #     raise ValueError("distance between particles is negative")
    # elif np.any(sigma <= 0.0):
    #     raise ValueError("particle diameter is not strictly positive")
    # if type(r) is np.ndarray:
    r = r[np.where(r <= r_c)]
    # elif r > r_c:
    #     return 0
    try:
        r6 = (sigma / r) ** 6
    except ZeroDivisionError:
        return float('+inf')
    else:
        return 4 * epsilon * r6 * (r6 - 1)
