from .particle import particle
from numpy import array, all


def test_boundary():
    tested = particle(size=5, dimension=2, mass=1, mode='hard', velocity=[])
    tested.size = 10
    tested.pos = array([0.0, 2.0, 12.0])
    tested.velocity = array([1.0, 3.0, 2.0])
    tested.hard_boundary()
    assert all(tested.pos == array([0.0, 2.0, 8.0]))
    assert all(tested.velocity == array([1.0, 3.0, -2.0]))
    tested.pos = array([0.0, 2.0, 12.0])
    tested.periodic_boundary()
    assert all(tested.pos == array([0.0, 2.0, 2.0]))
    assert all(tested.velocity == array([1.0, 3.0, -2.0]))
