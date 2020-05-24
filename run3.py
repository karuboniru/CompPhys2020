from matplotlib import pyplot as plt
from numpy import array, average, sqrt  # noqa

from molecular_dynamics import molecular_simluation

# seed(1)
count = 100
N = 10000
rho = 0.1
temp = 1.0
start = 0
interval = 100
timestep = 0.005
size = sqrt(count/rho)
sim = molecular_simluation(maxstep=N, temp=temp, count=count, size=size, mode='periodic',
                           dimension=2, rand=False, timestep=timestep, nu=1, interval=interval)
endtime = N*timestep
energylist = sim.energylist
end_energylist = array(energylist[len(energylist)//2:])
end_energylist_pow2 = end_energylist*end_energylist
avg = average(end_energylist)
line1, = plt.plot(
    [start + i*interval*timestep for i in range(len(energylist))], energylist)
line1.set_label('potenial energy')
line2 = plt.hlines(avg, xmin=0, xmax=endtime, linestyles='dashed')
line2.set_label('average after equilibration')

line3 = plt.hlines(average(energylist), xmin=0,
                   xmax=endtime, linestyles='dotted')
line3.set_label('average energy during simluation')
plt.legend()
print("average energy per particle", avg/count)
print("average energy", avg)
print("square fluctuation", (average(end_energylist_pow2) - avg**2))

print("fluctuation per particle", sqrt(
    (average(end_energylist_pow2) - avg**2))/count)
print("fluctuation", sqrt((average(end_energylist_pow2) - avg**2)))
plt.xlabel('time')
plt.ylabel('energy')
plt.savefig('fig/md_plot_norand_hard_'+str(N)+'_steps_'+str(count)+'_particles_' +
            str(rho)+'_rho_'+str(temp)+'_tempure_'+'.eps', format='eps')
# plt.savefig('fig/starting_fig_md.eps', format='eps')
# plt.show()
