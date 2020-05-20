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

    def do_velocities_assign(self):
        for i in range(self.count):
            for j in range(self.dimension):
                self.velocity[i][j] = random() - 0.5
        sumv = np.average(self.velocity, axis=1)
        sumv2 = np.sum(self.velocity**2)/self.count
        fs = np.sqrt(self.dimension*self.temp/sumv2)
        for i in range(self.count):
            self.velocity[i] -= sumv
            self.velocity[i] *= fs
            self.particles[i] -= self.velocity[i]*self.time_step
