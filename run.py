from matplotlib import pyplot as plt
from numpy import average
from monte_carlo import monte_carlo_sim
N = 20000
sim = monte_carlo_sim(maxstep=N, temp=1, count=100,
                      size=31.62, mode='periodic', mass=1)

sim.do_simluation()
# plt.yscale('log')
# plt.xscale('log')
energylist = sim.get_energy_per_step()
# plt.plot([i for i in range(N)], energylist)
x = []
y = []
for i in sim.phy_sys.particles:
    x.append(i.pos[0])
    y.append(i.pos[1])
plt.scatter(x, y)
print(average(energylist[N-500:N-1]))
plt.show()
