from random import random

import numpy as np

from configuration import physics_system
from lennard_jones_potential import calc_system_force


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
        sumv = self.get_mass_center_velocity()
        sumv2 = self.get_square_velocity_per_particle()
        fs = np.sqrt(self.dimension*self.temp/sumv2)
        self.velocity -= sumv
        self.velocity *= fs
        self.last_particles = self.particles - self.velocity[i]*self.time_step

    def get_square_velocity_per_particle(self):
        return np.sum(self.velocity**2)/self.count

    def get_mass_center_velocity(self):
        return np.average(self.velocity, axis=0)

    def molecular_dynamics_iter(self, update_velocity=False):
        force = self.get_force()
        particles_new = 2*self.particles - self.last_particles + \
            self.time_step**2*force/self.mass
        if update_velocity:
            self.velocity = (
                particles_new - self.last_particles)/(2*self.time_step)
        self.last_particles = self.particles
        self.particles = particles_new

    def get_force(self):
        return calc_system_force(x=self.particles, mode=self.mode, size=self.size)

    def get_total_energy(self):
        return self.get_square_velocity_per_particle()*self.mass/2+self.get_potential_energy()
