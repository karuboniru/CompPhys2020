from matplotlib import pyplot as plt
from numpy import average, sqrt, array  # noqa
from numpy.linalg import norm

from monte_carlo import monte_carlo

count = 300
N = 800000
rho = 0.8442
temp = 0.728
size = sqrt(count/rho)
sim = monte_carlo(maxstep=N, temp=temp, count=count,
                  size=size, mode='periodic', dimension=2, rand=True)
c = array([0.5*size]*2)
particles = array(list(sim.phy_sys.particles) + [i+array([size, 0]) for i in sim.phy_sys.particles] +
                  [i+array([-size, 0]) for i in sim.phy_sys.particles] +
                  [i+array([0, size]) for i in sim.phy_sys.particles]
                  + [i+array([0, -size]) for i in sim.phy_sys.particles])
r = [norm(i-c) for i in sim.phy_sys.particles]
r = r[r<size/sqrt(2)]
plt.hist(r, bins=20)
plt.xlabel('Distance')
plt.ylabel('Count')
# plt.show()
plt.savefig('fig/rdf-exp1_300.eps', format='eps')
