from random import randint, random

from numpy import exp, array

from configuration import particle, physics_system


class physical_system_monte_carlo(physics_system):
    def __init__(self, count=None, size=None, dimension=None, mass=None, mode='hard', temp=None, rand=None):
        if rand:
            super().__init__(count=count, size=size,
                             dimension=dimension, mass=mass, mode=mode)
        else:
            pass  # TODO: #1 will assign ordered particles here
        self.temp = temp

    def Metropolis_iter(self):
        now_energy = self.get_potential_energy()
        to_be_replaced = randint(0, self.count - 1)
        backup = self.particles[to_be_replaced]
        self.particles[to_be_replaced] = particle(
            size=self.size, dimension=self.dimension, mass=self.mass, mode=self.mode)
        # self.particles[to_be_replaced].pos += array(
        #     [random() for i in range(self.dimension)])*2.5
        # self.particles[to_be_replaced].pos %= self.size
        new_energy = self.get_potential_energy()
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
