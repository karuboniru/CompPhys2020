from .particle import particle
from numpy import array, sum
from lennard_jones_potential import pair_potential


class physics_system(object):
    def __init__(self, count, size, dimension, mass, mode):
        self.particles = [
            particle(size=size, dimension=dimension, mass=mass, mode=mode) for i in range(count)]
        self.size = size
        self.count = count
        self.dimension = dimension
        self.mass = mass
        self.mode = mode

    def get_potential_energy(self):
        return pair_potential(array([i.get_pos() for i in self.particles]), mode=self.mode, size=self.size)

    def get_kinetic_energy(self):
        return sum([i.get_kinetic_energy() for i in self.particles])
