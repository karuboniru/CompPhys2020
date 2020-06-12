from .physics_system_mc import monte_carlo_system


class monte_carlo(object):
    def __init__(self, count, size, dimension, mode, temp, maxstep, rand=True,
                 start_recording=float("inf"), recording_interval=100, pressure_record=False,
                 pressure_count=100):
        self.phy_sys = monte_carlo_system(
            count, size, dimension, mode=mode, temp=temp, rand=rand)
        self.maxstep = maxstep
        self.count = count
        self.pressure_record = pressure_record
        self.pressure_count = pressure_count
        self.energy_per_step = []
        self.pressure_list = []
        self.start_recording = start_recording
        self.recording_interval = recording_interval
        self.do_simluation()
        self.phy_sys.reposition()

    def do_simluation(self):
        def maxd(i):
            # if i < 5*self.count:
            #     return 2
            # if i < 30*self.count:
            #     return 1
            # if i < 50*self.count:
            #     return 0.5
            # if i < 90*self.count:
            #     return 0.2
            return 1.0
        for i in range(self.maxstep):
            _, energy = self.phy_sys.Metropolis_iter(
                maxd(i), record_true_energy=((i > self.start_recording) and (i % self.recording_interval == 0)))
            if ((i > self.start_recording) and (i % self.recording_interval == 0)):
                self.energy_per_step.append(energy)
            # if i%10000 == 0:
            #     print('on step', i)
        if(self.pressure_record):
            for i in range(self.pressure_count):
                self.pressure_list.append(self.phy_sys.calc_pressure())
                self.phy_sys.Metropolis_iter(maxd=1.0, record_true_energy=False)


    def get_pressure(self):
        return self.pressure_list

    def get_energy_per_step(self):
        return self.energy_per_step
