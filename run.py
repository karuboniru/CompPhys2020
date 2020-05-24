from matplotlib import pyplot as plt
from numpy import average, sqrt  # noqa

from monte_carlo import monte_carlo

count = 100
N = 70000
rho = 1
temp = 0.0
size = sqrt(count/rho)
sim = monte_carlo(maxstep=N, temp=temp, count=count,
                  size=size, mode='periodic', dimension=2, rand=True)


# plt.yscale('log')
# plt.xscale('log')
energylist = sim.get_energy_per_step()
# plt.plot([i for i in range(N)], energylist)
x = []
y = []
for i in sim.phy_sys.particles:
    x.append(i[0])
    y.append(i[1])
plt.scatter(x, y)
plt.xlabel('x')
plt.ylabel('y')
print(sim.phy_sys.get_potential_energy()/count)
plt.show()
# plt.savefig('fig/rand_scatter_'+str(N)+'_steps_'+str(count)+'_particles_'+str(rho)+'_rho_'+str(temp)+'_tempure_.eps', format='eps')
