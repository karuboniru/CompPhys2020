from matplotlib import pyplot as plt
from numpy import average, sqrt, array  # noqa
from monte_carlo import monte_carlo_sim

count = 300
N = 70000
rho = 0.8442
temp = 0.728
start = 0
interval = 200
size = sqrt(count/rho)
sim = monte_carlo_sim(maxstep=N, temp=temp, count=count, size=size, mode='periodic',
                      mass=1, dimension=2, rand=False, start_recording=start, recording_interval=interval)

# plt.yscale('log')
# plt.xscale('log')
energylist = sim.get_energy_per_step()
end_energylist = array(energylist[len(energylist)//2:])
end_energylist_pow2 = end_energylist*end_energylist
avg = average(end_energylist)
plt.plot([start + i*interval for i in range(len(energylist))], energylist)
plt.hlines(avg, xmin=0, xmax=N)

print("average energy per particle", avg/count)
print("fluctuation per particle", (average(end_energylist_pow2) - avg**2)/count)
plt.show()
