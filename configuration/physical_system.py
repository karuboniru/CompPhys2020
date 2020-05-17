# from .particle import particle
from numpy import array, sum
from lennard_jones_potential import pair_potential, potential_for_one_particle
from random import random


class physics_system(object):
    def __init__(self, count, size, dimension, mass, mode, velocity=None):
        self.particles = array([
            [random()*size for j in range(dimension)] for i in range(count)])
        self.velocity = velocity
        self.size = size
        self.count = count
        self.dimension = dimension
        self.mass = mass
        self.mode = mode

    def get_potential_energy(self):
        return pair_potential(self.particles, mode=self.mode, size=self.size)

    def get_potential_energy_for_one(self, particle_id):
        return potential_for_one_particle(self.particles, particle_id=particle_id, mode=self.mode, size=self.size)

    def get_kinetic_energy(self):
        return sum([i.get_kinetic_energy() for i in self.particles])

    def periodic_boundary(self, particle_id):
        self.particles[particle_id] %= self.size

    def hard_boundary(self, particle_id):
        if_out = ((self.particles[particle_id] % self.size - self.particles[particle_id]) != 0) * \
            (-1)+((self.particles[particle_id] %
                   self.size - self.particles[particle_id]) == 0)*1
        self.particles[particle_id] = (
            self.particles[particle_id]*if_out) % self.size
        if (self.velocity is not None):
            self.velocity[particle_id] *= if_out

    def random_displace(self, particle_id, maxd=0.25):
        self.particles[particle_id] += array(
            [random()-0.5 for i in range(self.dimension)])*maxd  # maybe better than just random place
        self.reposition(particle_id)

    def reposition(self, particle_id):
        if self.mode == 'hard':
            self.hard_boundary(particle_id)
        if self.mode == 'periodic':
            self.periodic_boundary(particle_id)
