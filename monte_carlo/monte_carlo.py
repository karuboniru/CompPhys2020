from .physics_system_mc import physical_system_monte_carlo


class monte_carlo_sim(object):
    def __init__(self, count, size, dimension, mass, mode, temp, maxstep, rand=True, start_recording=float("inf"), recording_interval=100):
        self.phy_sys = physical_system_monte_carlo(
            count, size, dimension, mass, mode=mode, temp=temp, rand=rand)
        self.maxstep = maxstep
        self.count = count
        self.energy_per_step = []
        self.start_recording = start_recording
        self.recording_interval = recording_interval
        self.do_simluation()

    def do_simluation(self):
        def maxd(i):
            if i < 5*self.count:
                return 2
            if i < 30*self.count:
                return 1
            if i < 50*self.count:
                return 0.5
            if i < 90*self.count:
                return 0.2
            return 0.1
        for i in range(self.maxstep):
            _, energy = self.phy_sys.Metropolis_iter(
                maxd(i), record_true_energy=((i > self.start_recording) and (i % self.recording_interval == 0)))
            if ((i > self.start_recording) and (i % self.recording_interval == 0)):
                self.energy_per_step.append(energy)

    def get_energy_per_step(self):
        return self.energy_per_step
