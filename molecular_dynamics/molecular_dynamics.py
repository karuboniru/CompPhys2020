from .molecular_dynamics_system import molecular_dynamics_system


class molecular_simluation(object):
    def __init__(self, count, size, dimension, mass, mode, temp, maxstep, timestep, rand):
        self.phy_sys = molecular_dynamics_system(
            count, size, dimension, mass, mode, temp, rand, timestep)
        self.maxstep = maxstep
        self.init_energy = self.phy_sys.get_total_energy()

    def do_simluation(self):
        for i in range(self.maxstep):
            self.phy_sys.molecular_dynamics_iter()

    def begin_simluation(self):
        self.do_simluation()
        # self.phy_sys.reposition()
        self.after_energy = self.phy_sys.get_total_energy()