from configuration import physics_system
from numpy import array, all


def test_boundary_hard():
    tested = physics_system(size=5, dimension=2,
                            mode='hard', velocity=[], count=1)
    tested.size = 10
    tested.particles = array([[0.0, 2.0, 12.0]])
    tested.velocity = array([[1.0, 3.0, 2.0]])
    tested.reposition(0)
    assert all(tested.particles == array([[0.0, 2.0, 8.0]]))
    assert all(tested.velocity == array([[1.0, 3.0, -2.0]]))


def test_boundary_periodic():
    tested = physics_system(size=5, dimension=2,
                            mode='periodic', velocity=[], count=1)
    tested.size = 10
    tested.particles = array([[0.0, 2.0, 12.0]])
    tested.velocity = array([[1.0, 3.0, 2.0]])
    tested.particles = array([[0.0, 2.0, 12.0]])
    tested.reposition(0)
    assert all(tested.particles == array([[0.0, 2.0, 2.0]]))
    assert all(tested.velocity == array([[1.0, 3.0, 2.0]]))
