from .particle import particle
from numpy import array, sum
from lennard_jones_potential import pair_potential


class physics_system(object):
    def __init__(self, count=30, size=5, dimension=2, mass=1, mode='hard'):
        self.particles = [
            particle(size=size, dimension=dimension, mass=mass, mode=mode) for i in range(count)]
        self.size = size

    def get_potential_energy(self):
        return pair_potential(array([i.get_pos() for i in self.particles]))

    def get_kinetic_energy(self):
        return sum([i.get_kinetic_energy() for i in self.particles])
