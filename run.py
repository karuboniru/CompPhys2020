from matplotlib import pyplot as plt
from numpy import average
from monte_carlo import monte_carlo_sim
N = 10000
sim = monte_carlo_sim(maxstep=N, temp=1, count=100, size=31.622)

sim.do_simluation()
# plt.yscale('log')
plt.xscale('log')
energylist = sim.get_energy_per_step()
plt.plot([i for i in range(N)], energylist)
print(average(energylist[N-500:N-1]))
plt.show()
