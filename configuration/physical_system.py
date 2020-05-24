# from .particle import particle
from random import random

from numpy import array, empty, sqrt, add, mod

from lennard_jones_potential import pair_potential, potential_for_one_particle


class physics_system(object):
    def __init__(self, count, size, dimension, mode, velocity=None, rand=True):
        self.size = size
        self.count = count
        self.dimension = dimension
        self.mode = mode
        if rand:
            self.particles = array([
                [random()*size for j in range(dimension)] for i in range(count)])
        else:
            self.particles = empty((count, dimension))
            self.hex_place(dimension)
        self.velocity = velocity

    def no_overlap(self):
        for i in range(self.count):
            while True:
                if(self.get_potential_energy_for_one(i) == float('inf')):
                    self.particles[i] = [
                        random()*self.size for j in range(self.dimension)]
                else:
                    break

    def get_potential_energy(self):
        return pair_potential(self.particles, mode=self.mode, size=self.size)

    def get_potential_energy_for_one(self, particle_id):
        return potential_for_one_particle(self.particles, particle_id=particle_id, mode=self.mode, size=self.size)

    # def periodic_boundary(self, particle_id):
    #     self.particles[particle_id] %= self.size

    def hard_boundary(self, particle_id=None):
        if particle_id is not None:
            if_out = ((self.particles[particle_id] % self.size - self.particles[particle_id]) != 0) * \
                (-1)+((self.particles[particle_id] %
                       self.size - self.particles[particle_id]) == 0)*1
            self.particles[particle_id] = (
                self.particles[particle_id]*if_out) % self.size
            if (self.velocity is not None):
                self.velocity[particle_id] *= if_out
        else:
            if_out = ((self.particles % self.size - self.particles) != 0) * \
                (-1)+((self.particles % self.size - self.particles) == 0)*1
            self.particles = (self.particles*if_out) % self.size
            if (self.velocity is not None):
                self.velocity *= if_out

    def periodic_boundary(self):
        self.particles %= self.size

    def reposition(self, particle_id=None):
        if self.mode == 'hard':
            self.hard_boundary(particle_id)
        if self.mode == 'periodic':
            self.periodic_boundary()

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


def reduce(r, size):
    add(r, size/2, out=r)
    mod(r, size, out=r)
    add(r, -size/2, out=r)
    return r
