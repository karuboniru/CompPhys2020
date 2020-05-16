import numpy as np

from .lennard_jones import lennard_jones


def pair_potential(x, mode, size=None, sigma=1.0, epsilon=1.0, r_c=2.5):
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
    position_difference_list = x[left] - x[right]
    if mode == 'hard':
        pass
    elif mode == 'periodic':
        # following code will generate copies of position_difference_list on every calculation
        # r = np.linalg.norm((np.abs(position_difference_list)+size/2) %
        #                    size-size/2, axis=1)
        # this code below can avoid creating copies of array position_difference_list, can make code faster
        # because position_difference_list is a bug list (N^2/2) avoiding coping this will be helpful
        np.abs(position_difference_list, out=position_difference_list)
        np.add(position_difference_list, size/2, out=position_difference_list)
        np.mod(position_difference_list, size, out=position_difference_list)
        np.add(position_difference_list, -size/2, out=position_difference_list)
    else:
        raise ValueError('Wrong mode specified')
    return np.sum(lennard_jones(np.linalg.norm(
        position_difference_list, axis=1), sigma=sigma, epsilon=epsilon, r_c=r_c))
