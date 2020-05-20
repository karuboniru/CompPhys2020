from random import random

import numpy as np

from configuration import physics_system


class molecular_dynamics_system(physics_system):
    def __init__(self, count, size, dimension, mass, mode, temp, rand, time_step):
        # init a physical system with random place and we will assign velocities later
        super().__init__(count=count, size=size, dimension=dimension, mass=mass,
                         mode=mode, rand=rand, velocity=np.empty((count, dimension)))
        self.temp = temp
        self.time_step = time_step
        # assign velocities
        self.do_velocities_assign()
        if mode == 'hard':
            self.boundary = self.hard_boundary
        elif mode == 'periodic':
            self.boundary = self.periodic_boundary
        else:
            raise(ValueError)

    def do_velocities_assign(self):
        for i in range(self.count):
            for j in range(self.dimension):
                self.velocity[i][j] = random() - 0.5
        sumv = np.average(self.velocity, axis=0)
        sumv2 = np.sum(self.velocity**2)/self.count
        fs = np.sqrt(self.dimension*self.temp/sumv2)
        for i in range(self.count):
            self.velocity[i] -= sumv
            self.velocity[i] *= fs
            self.particles[i] -= self.velocity[i]*self.time_step

    def periodic_boundary(self):
        self.particles %= self.size

    def hard_boundary(self):
        if_out = ((self.particles % self.size - self.particles) != 0) * \
            (-1)+((self.particles % self.size - self.particles) == 0)*1
        self.particles = (self.particles*if_out) % self.size
        if (self.velocity is not None):
            self.velocity *= if_out
