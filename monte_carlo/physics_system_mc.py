import copy
from random import randint, random

from numpy import exp

from configuration import particle, physics_system


class physical_system_monte_carlo(physics_system):
    def __init__(self, count=30, size=5, dimension=2, mass=1, mode='hard', temp=10, rand=True):
        if rand:
            super().__init__(count=count, size=size,
                             dimension=dimension, mass=mass, mode=mode)
        else:
            pass  # TODO: #1 will assign ordered particles here
        self.temp = temp

    def Metropolis_iter(self):
        now_energy = self.get_potential_energy()
        to_be_replaced = randint(0, self.count - 1)
        new_configuration = copy.deepcopy(self)
        new_configuration.particles[to_be_replaced] = particle(
            size=self.size, dimension=self.dimension, mass=self.mass, mode=self.mode)
        new_energy = new_configuration.get_potential_energy()
        if new_energy < now_energy:
            self.particles = new_configuration.particles
            return True, new_energy
        if self.temp == 0:
            return False, now_energy
        if random() < exp((now_energy - new_energy)/self.temp):
            self.particles = new_configuration.particles
            return True, new_energy
        else:
            return False, now_energy
