from random import randint, random
from functools import partial
from numpy import exp
from copy import deepcopy

from configuration import physics_system


class physical_system_monte_carlo(physics_system):
    def __init__(self, count, size, dimension, mass, mode, temp, rand):
        super().__init__(count=count, size=size,
                         dimension=dimension, mass=mass, mode=mode, rand=rand)
        self.temp = temp

    def Metropolis_iter(self, maxd, record_true_energy=False):
        to_be_replaced = randint(0, self.count - 1)
        if record_true_energy:
            self.get_energy_method = self.get_potential_energy
        else:
            self.get_energy_method = partial(self.get_potential_energy_for_one, particle_id=to_be_replaced)
        now_energy = self.get_energy_method()
        # if not deepcopy, backup will only be a "reference"
        backup = deepcopy(self.particles[to_be_replaced])
        # --------------------------way 1
        # self.particles[to_be_replaced] = particle(
        #     size=self.size, dimension=self.dimension, mass=self.mass, mode=self.mode)
        # --------------------------way 2
        # self.particles[to_be_replaced].pos += array(
        #     [random()-0.5 for i in range(self.dimension)])*2.5  # maybe better than just random place
        # self.particles[to_be_replaced].replace()
        # --------------------------way 3
        self.random_displace(to_be_replaced, maxd)
        new_energy = self.get_energy_method()
        if new_energy < now_energy:
            return True, new_energy
        if self.temp == 0:
            self.particles[to_be_replaced] = backup
            return False, now_energy
        if random() < exp((now_energy - new_energy)/self.temp):
            return True, new_energy
        else:
            self.particles[to_be_replaced] = backup
            return False, now_energy
