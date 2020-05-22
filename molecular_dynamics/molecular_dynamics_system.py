from random import random, gauss

import numpy as np

from configuration import physics_system, reduce
from lennard_jones_potential import calc_system_force
from monte_carlo import monte_carlo_sim


class molecular_dynamics_system(physics_system):
    def __init__(self, count, size, dimension, mode, temp, rand, time_step, nu=0.1):
        # init a physical system with random place and we will assign velocities later
        if rand:
            self.size = size
            self.count = count
            self.dimension = dimension
            self.nu = nu
            self.mode = mode
            self.particles = monte_carlo_sim(
                count, size, dimension, mode, temp, 3000, rand).phy_sys.particles
            self.velocity = np.empty((count, dimension))
        else:
            super().__init__(count=count, size=size, dimension=dimension,
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
        sumv2 = self.get_square_velocity()/self.count
        fs = np.sqrt(self.dimension*self.temp/sumv2)
        self.velocity -= sumv
        self.velocity *= fs
        self.last_particles = self.particles - self.velocity*self.time_step

    def get_square_velocity(self):
        return np.sum(self.velocity**2)

    def get_mass_center_velocity(self):
        return np.average(self.velocity, axis=0)

    def molecular_dynamics_iter(self, update_velocity=True):
        force = self.get_force()
        self.reposition()
        particles_new = 2*self.particles - self.last_particles + \
            self.time_step**2*force
        if update_velocity:
            self.velocity = reduce(
                particles_new - self.last_particles, self.size)/(2*self.time_step)
        self.last_particles = self.particles
        self.particles = particles_new
        self.reposition()

    def molecular_dynamics_iter_mothod_1(self, update_velocity=True):
        force = self.get_force()
        self.particles += self.time_step*self.velocity + 0.5*self.time_step**2*force
        self.velocity += self.time_step*force

    def get_force(self):
        return calc_system_force(x=self.particles, mode=self.mode, size=self.size)

    def get_total_energy(self):
        return self.get_square_velocity()/2+self.get_potential_energy()

    def molecular_dynamics_iter_heat(self, update_velocity=True):
        self.molecular_dynamics_iter()
        # Andersen heat bath
        # self.velocity += dv
        tempa = self.get_square_velocity()
        temp = tempa/(self.dimension*self.count)
        for i in range(self.count):
            if(random() < self.nu*self.time_step):
                for j in range(self.dimension):
                    self.velocity[i][j] = gauss(mu=0, sigma=np.sqrt(self.temp))
        self.last_particles = self.particles - self.velocity*self.time_step
