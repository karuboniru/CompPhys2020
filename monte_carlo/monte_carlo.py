from .physics_system_mc import physical_system_monte_carlo


class monte_carlo_sim(object):
    def __init__(self, count, size, dimension, mass, mode, temp, maxstep, rand=True):
        self.phy_sys = physical_system_monte_carlo(
            count, size, dimension, mass, mode=mode, temp=temp, rand=rand)
        self.maxstep = maxstep
        self.energy_per_step = [None]*maxstep

    def do_simluation(self):
        for i in range(self.maxstep):
            _, self.energy_per_step[i] = self.phy_sys.Metropolis_iter()

    def get_energy_per_step(self):
        return self.energy_per_step
