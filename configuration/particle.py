from random import random

from numpy import array
from numpy.linalg import norm


class particle(object):
    def __init__(self, size=5, dimension=2, mass=1, mode='hard', velocity=[]):
        self.pos = array([random()*size for i in range(dimension)])
        if velocity == []:
            self.velocity = array([0] * dimension)
        else:
            self.velocity = array(velocity)
        self.mass = mass
        self.mode = mode
        self.size = size
        self.dimension = dimension

    def periodic_boundary(self):
        self.pos %= self.size

    def hard_boundary(self):
        if_out = ((self.pos % self.size - self.pos) != 0) * \
            (-1)+((self.pos % self.size - self.pos) == 0)*1
        self.velocity *= if_out
        self.pos = (self.pos*if_out) % self.size

    def get_pos(self):
        return self.pos

    def step(self, force, step_time):
        acceleration = force/self.mass
        self.pos += self.velocity*step_time + acceleration*step_time**2
        self.velocity = acceleration*step_time
        if self.mode == 'hard':
            self.hard_boundary()
        if self.mode == 'periodic':
            self.periodic_boundary()

    def get_kinetic_energy(self):
        return 0.5*self.mass*norm(self.velocity)
