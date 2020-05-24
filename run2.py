from matplotlib import pyplot as plt
from numpy import array, average, sqrt  # noqa

from monte_carlo import monte_carlo

count = 100
N = 100000
rho = 0.8442
temp = 0.728
start = 0
interval = 200
rand = False
size = sqrt(count/rho)
sim = monte_carlo(maxstep=N, temp=temp, count=count, size=size, mode='periodic',
                  dimension=2, rand=rand, start_recording=start, recording_interval=interval)

# plt.yscale('log')
# plt.xscale('log')
energylist = sim.get_energy_per_step()
end_energylist = array(energylist[len(energylist)//2:])
end_energylist_pow2 = end_energylist*end_energylist
avg = average(end_energylist)
line1, = plt.plot(
    [start + i*interval for i in range(len(energylist))], energylist)
line1.set_label('potenial energy')
line2 = plt.hlines(avg, xmin=0, xmax=N, linestyles='dashed')
line2.set_label('average after equilibration')

line3 = plt.hlines(average(energylist), xmin=0, xmax=N, linestyles='dotted')
line3.set_label('average energy during simluation')
plt.legend()
print("average energy per particle", avg/count)
print("fluctuation per particle", (average(end_energylist_pow2) - avg**2)/count)
plt.savefig('fig/plot_'+str(N)+'_steps_'+str(count)+'_particles_' +
            str(rho)+'_rho_'+str(temp)+'_tempure_'+str(rand)+'.eps', format='eps')

# plt.show()
