import numpy as np
from lennard_jones_potential.lennard_jones import lennard_jones


def pair_potential(x, args=()):
    """

    Calculates the potential energy of configuration of particles.

    >>> from ljpotential import lennard_jones_potential as lj

    >>> x = np.array([[0.0, 0.0, 0.0]])
    >>> pair_potential(x)
    0.0

    >>> x = np.array([[0.0, 0.0, 0.0], [0.0, 0.0, 1.0]])
    >>> pair_potential(x)
    0.0
    >>> pair_potential(x)
    0.0

    >>> x = np.array([[0.0, 0.0], [0.0, 1.0], [0.0, 2.0]])
    >>> pair_potential(x, args=(1.0, 1.0))  #doctest: +ELLIPSIS
    -0.061523...

    :param x: positions of the particles
    :type x: list of lists
    :param potential: the pairwise potential function.
                      must be of the form f(x, *args).
    :type potential: callable
    :param args: arguments to pass to the function

    :return: energy of the configuration
    :rtype: float
    """


    n, _ = x.shape
    left, right = np.triu_indices(n, 1)
    r = np.linalg.norm(x[left] - x[right], axis=1)
    energy = np.sum(lennard_jones(r, *args))

    return energy
