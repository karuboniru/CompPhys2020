# from .particle import particle
from numpy import array, sum, sqrt, empty
from lennard_jones_potential import pair_potential, potential_for_one_particle
from random import random


class physics_system(object):
    def __init__(self, count, size, dimension, mass, mode, velocity=None, rand=True):
        self.size = size
        self.count = count
        self.dimension = dimension
        self.mass = mass
        self.mode = mode
        if rand:
            self.particles = array([
                [random()*size for j in range(dimension)] for i in range(count)])
        else:
            self.particles = empty((count, dimension))
            self.hex_place(dimension)
        self.velocity = velocity

    def get_potential_energy(self):
        return pair_potential(self.particles, mode=self.mode, size=self.size)

    def get_potential_energy_for_one(self, particle_id):
        return potential_for_one_particle(self.particles, particle_id=particle_id, mode=self.mode, size=self.size)

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

    def hex_place(self, dimension):
        if dimension != 2:
            raise(NotImplementedError)
        n = int(sqrt(self.count))
        k = 0
        lam = 1.1
        for i in range(n):
            for j in range(n):
                self.particles[k][0] = (i*sqrt(3) / 2)*lam
                self.particles[k][1] = ((i % 2 != 0)*(1/2) + j)*lam
                k += 1
        remain = self.count - n**2
        for g in range(remain):
            self.particles[k][0] = (n*sqrt(3) / 2)*lam
            self.particles[k][1] = ((n % 2 != 0)*(1/2) + g)*lam
            k += 1
