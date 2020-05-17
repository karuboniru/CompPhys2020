from matplotlib import pyplot as plt
from numpy import average, sqrt
from monte_carlo import monte_carlo_sim
N = 10000
count = 100
rho = 0.8442
temp = 0.728
size = sqrt(count/rho)
sim = monte_carlo_sim(maxstep=N, temp=temp, count=count,
                      size=size, mode='periodic', mass=1, dimension=2)

sim.do_simluation()
# plt.yscale('log')
# plt.xscale('log')
energylist = sim.get_energy_per_step()
# plt.plot([i for i in range(N)], energylist)
x = []
y = []
for i in sim.phy_sys.particles:
    x.append(i[0])
    y.append(i[1])
    x.append(i[0]+size)
    y.append(i[1])
    x.append(i[0]-size)
    y.append(i[1])
    x.append(i[0])
    y.append(i[1]+size)
    x.append(i[0])
    y.append(i[1]-size)
    x.append(i[0]+size)
    y.append(i[1]+size)
    x.append(i[0]-size)
    y.append(i[1]+size)
    x.append(i[0]+size)
    y.append(i[1]-size)
    x.append(i[0]-size)
    y.append(i[1]-size)
plt.scatter(x, y)
print(sim.phy_sys.get_potential_energy())
plt.show()
