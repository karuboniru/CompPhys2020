import numpy as np

from .calc_total_energy import pair_potential
from .lennard_jones import lennard_jones
import pytest


def test_lennard_jones():
    assert lennard_jones(2**(1/6), 1.0, 1.0) == -1.0
    assert lennard_jones(10.0, 1.0, 1.0, 2.5) == 0
    with pytest.raises(ValueError, match='distance between particles is negative'):
        lennard_jones(-1.0, 1.0, 1.0)
    with pytest.raises(ValueError, match='particle diameter is not strictly positive'):
        lennard_jones(1.0, -1.0, 1.0)
    with pytest.raises(ZeroDivisionError):
        lennard_jones(0.0, 1.0, 1.0)


def test_pair_potential():
    assert pair_potential(np.array([[0, 0, 0]]), mode='hard') == 0.0
    assert pair_potential(
        np.array([[0.0, 0.0], [0.0, 1.0], [0.0, 2.0]]), mode='hard') == -0.0615234375
    assert pair_potential(
        np.array([[0.0, 0.0], [0.0, 2.51]]), mode='hard') == 0
    assert pair_potential(np.array([[0.0, 0.0], [0.0, 2.0]]), mode='periodic', size=3.0) == pair_potential(
        np.array([[0.0, 0.0], [0.0, 1.0]]), mode='periodic', size=3.0)
    assert pair_potential(
        np.array([[0.0, 0.0], [0.0, 1.1]]), r_c=0.5, mode='hard') == 0
    with pytest.raises(ValueError):
        pair_potential(
            np.array([[0.0, 0.0], [0.0, 2.51]]), mode='something else')
    assert pair_potential(
        np.array([[0.0, 0.0], [0.0, 1.0]]), mode='hard') == lennard_jones(1.0)
    assert abs(pair_potential(np.array([[0.0, 0.0], [0.0, 0.2]]), mode='hard') -
               pair_potential(np.array([[0.0, 0.0], [0.0, 0.2]]), mode='periodic', size=10)) < 0.001
