from matplotlib import pyplot as plt
from numpy import average, sqrt, array  # noqa
from molecular_dynamics import molecular_simluation

count = 30
N = 10000
rho = 0.8442
temp = 0.728
start = 0
interval = 200
size = sqrt(count/rho)
sim = molecular_simluation(maxstep=N, temp=temp, count=count, size=size, mode='periodic',
                           mass=1, dimension=2, rand=True, timestep=0.001)

# plt.yscale('log')
# plt.xscale('log')
x = []
y = []
for i in sim.phy_sys.particles:
    x.append(i[0])
    y.append(i[1])
plt.scatter(x, y)
plt.show()
