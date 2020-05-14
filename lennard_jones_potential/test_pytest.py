from lennard_jones_potential.lennard_jones import lennard_jones
from lennard_jones_potential.calc_total_energy import pair_potential
import numpy as np
def test_lennard_jones():
    assert lennard_jones(2**(1/6), 1.0, 1.0) == -1.0
    assert lennard_jones(10.0, 1.0, 1.0, 2.5) == 0

def test_pair_potential():
    assert pair_potential(np.array([[0,0,0]])) == 0.0
    assert pair_potential(np.array([[0.0, 0.0], [0.0, 1.0], [0.0, 2.0]])) == -0.0615234375
    assert pair_potential(np.array([[0.0, 0.0], [0.0, 2.51]])) == 0