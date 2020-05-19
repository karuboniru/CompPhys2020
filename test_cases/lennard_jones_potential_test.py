import numpy as np

from lennard_jones_potential.calc_total_energy import pair_potential
from lennard_jones_potential.lennard_jones import lennard_jones
import pytest


def lennard_jones_single(r, sigma=1.0, epsilon=1.0, r_c=2.5):
    return np.sum(lennard_jones(np.array([r]), sigma=1.0, epsilon=1.0, r_c=2.5))


def near(x, y):
    return abs(x-y) < 1e-8*(max([abs(x), abs(y)]))


def test_lennard_jones_single_special_number():
    assert lennard_jones_single(2**(1/6), 1.0, 1.0) == -1.0
    assert lennard_jones_single(10.0, 1.0, 1.0, 2.5) == 0
    with np.errstate(divide='ignore'):
        assert lennard_jones_single(0, 1.0, 1.0, 2.5) == float('+inf')

# no more need this
# def test_lennard_jones_single_with_expections():
#     with pytest.raises(ValueError, match='distance between particles is negative'):
#         lennard_jones_single(-1.0, 1.0, 1.0)
#     with pytest.raises(ValueError, match='particle diameter is not strictly positive'):
#         lennard_jones_single(1.0, -1.0, 1.0)
#     with pytest.raises(ZeroDivisionError):
#         lennard_jones_single(0.0, 1.0, 1.0)


def test_pair_potential():
    assert pair_potential(np.array([[0, 0, 0]]), mode='hard') == 0.0


def test_pair_potential_special_number():
    assert near(pair_potential(
        np.array([[0.0, 0.0], [0.0, 1.0], [0.0, 2.0]]), mode='hard'), -0.0615234375)
    assert pair_potential(
        np.array([[0.0, 0.0], [0.0, 1.0]]), mode='hard') == lennard_jones_single(1.0)


def test_pair_potential_out_of_range():
    assert pair_potential(
        np.array([[0.0, 0.0], [0.0, 2.51]]), mode='hard') == 0
    assert pair_potential(
        np.array([[0.0, 0.0], [0.0, 1.1]]), r_c=0.5, mode='hard') == 0


def test_pair_periodic():
    assert near(pair_potential(
        np.array([[0.0], [0.4]]), mode='periodic', size=1.0), lennard_jones_single(0.4))
    assert near(pair_potential(
        np.array([[0.0], [0.6]]), mode='periodic', size=1.0), lennard_jones_single(0.4))
    assert near(pair_potential(
        np.array([[0.0], [-0.4]]), mode='periodic', size=1.0), lennard_jones_single(0.4))
    assert near(pair_potential(
        np.array([[0.0], [-0.6]]), mode='periodic', size=1.0), lennard_jones_single(0.4))


def test_pair_periodic_with_expections():
    with pytest.raises(ValueError):
        pair_potential(
            np.array([[0.0, 0.0], [0.0, 2.51]]), mode='something else')
