from configuration import physics_system, particle
from random import randint, random
from numpy import exp
import copy


class physical_system_monte_carlo(physics_system):
    def __init__(self, mcount=30, msize=5, mdimension=2, mmass=1, mmode='hard', temp=10):
        super().__init__(count=mcount, size=msize,
                         dimension=mdimension, mass=mmass, mode=mmode)
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
        else:
            if self.temp == 0:
                return
            if random() > exp((now_energy - new_energy)/self.temp):
                self.particles = new_configuration.particles
