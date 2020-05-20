from .molecular_dynamics_system import molecular_dynamics_system


class molecular_simluation(object):
    def __init__(self, count, size, dimension, mass, mode, temp, maxstep, timestep, rand=True):
        self.phy_sys = molecular_dynamics_system(
            count, size, dimension, mass, mode, temp, rand, timestep)
        self.maxstep = maxstep
        self.do_simluation()

    def do_simluation(self):
        for i in range(self.maxstep):
            self.phy_sys.molecular_dynamics_iter()
