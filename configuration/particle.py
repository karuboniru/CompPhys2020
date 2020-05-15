from random import random

from numpy import array, any
from numpy.linalg import norm


class particle(object):
    def init(self, size, dimension, mass=1, mode = 'hard'):
        self.pos = array([random()*size for i in range(dimension)])
        self.velocity = array([0] * dimension)
        self.mass = mass
        self.mode = mode
        self.size = size

    def get_pos(self):
        return self.pos

    def step(self, force, step_time):
        acceleration = force/self.mass
        self.pos += self.velocity*step_time + self.acceleration*step_time**2
        self.velocity = self.acceleration*step_time
        if any(self.pos<0):
            pass

    def get_kinetic_energy(self):
        return 0.5*self.mass*norm(self.velocity)
