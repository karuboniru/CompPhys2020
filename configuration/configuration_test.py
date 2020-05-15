from .particle import *
from numpy import array, all


class Test(particle):
    def test_boundary(self):
        self.size = 10
        self.pos = array([0.0, 2.0, 12.0])
        self.velocity = array([1.0, 3.0, 2.0])
        self.hard_boundary()
        assert all(self.pos == array([0.0, 2.0, 8.0]))
        assert all(self.velocity == array([1.0, 3.0, -2.0]))
        self.pos = array([0.0, 2.0, 12.0])
        self.periodic_boundary()
        assert all(self.pos == array([0.0, 2.0, 2.0]))
        assert all(self.velocity == array([1.0, 3.0, -2.0]))
