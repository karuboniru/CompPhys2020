from matplotlib import pyplot as plt  # noqa
from numpy import average, sqrt  # noqa
from monte_carlo import monte_carlo
import cProfile


def run():
    count = 500
    N = 10000
    rho = 0.8442
    temp = 0.728
    size = sqrt(count/rho)
    sim = monte_carlo(maxstep=N, temp=temp, count=count,
                      size=size, mode='periodic', dimension=2, rand=False, start_recording=9000)

    # plt.yscale('log')
    # plt.xscale('log')
    # energylist = sim.get_energy_per_step()
    # plt.plot([i for i in range(N)], energylist)
    x = []
    y = []
    for i in sim.phy_sys.particles:
        x.append(i[0])
        y.append(i[1])


cProfile.run('run()')
