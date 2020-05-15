from configuration import physical_system, particle
from random import randint
import copy


class physical_system_mc(physical_system):
    def __init__(self, count=30, size=5, dimension=2, mass=1, mode='hard', temp=10):
        super().__init__(self, count=count, size=size,
                         dimension=dimension, mass=mass, mode=mode)
        self.temp = temp

    def Metropolis_iter(self):
        now_energy = self.get_potential_energy()
        to_be_replaced = randint(0, self.count - 1)
        new_configuration = copy.deepcopy(self)
        new_configuration.particles[to_be_replaced] = particle(
            size=self.size, dimension=self.dimension, mass=self.mass, mode=self.mode)
        new_energy = new_configuration.get_potential_energy()
        if new_energy<now_energy:
            pass
        else:
            pass
