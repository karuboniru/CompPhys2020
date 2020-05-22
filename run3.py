from matplotlib import pyplot as plt
from numpy import average, sqrt, array  # noqa
from molecular_dynamics import molecular_simluation
from random import seed
seed(1)
count = 32
N = 1000
rho = 0.8442
temp = 0.728
start = 0
interval = 200
size = sqrt(count/rho)
sim = molecular_simluation(maxstep=N, temp=temp, count=count, size=size, mode='periodic',
                           dimension=2, rand=True, timestep=0.005, nu=0.01)

print("ke:", sim.phy_sys.get_square_velocity() /
      2, "po", sim.phy_sys.get_potential_energy())
# print(sim.phy_sys.particles)
print(sim.phy_sys.get_potential_energy())
sim.begin_simluation()
# print("ke:", sim.phy_sys.get_square_velocity() /
#       2, "po", sim.phy_sys.get_potential_energy())
# print(sim.phy_sys.particles)
# sim.phy_sys.reposition()
# plt.yscale('log')
# plt.xscale('log')
print(sim.phy_sys.get_mass_center_velocity())
print(sim.phy_sys.get_potential_energy())

x = []
y = []
for i in sim.phy_sys.particles:
    x.append(i[0])
    y.append(i[1])
plt.scatter(x, y)
plt.show()
