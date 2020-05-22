import numpy as np


def calc_force(r, r_c, mode, size, sigma, epsilon):
    _, d = r.shape
    if mode == 'periodic':
        np.add(r, size/2, out=r)
        np.mod(r, size, out=r)
        np.add(r, -size/2, out=r)
    nr_tmp = np.linalg.norm(r, axis=1)
    # nr_tmp = np.where(nr_tmp == 0.0, 1e-2, nr_tmp)
    nr = np.transpose(np.array([nr_tmp for i in range(d)]))
    # if(nr >= r_c):
    #     return np.array(np.zeros_like(r))
    return (nr <= r_c)*4*epsilon*(12*sigma**12/nr**14 - 6*sigma**6/nr**8)*r


def calc_system_force(x, mode, size=None, sigma=1.0, epsilon=1.0, r_c=2.5):
    n, _ = x.shape
    left, right = np.triu_indices(n, 1)
    force = np.zeros_like(x)
    dr = x[left] - x[right]
    forcelist = calc_force(dr, r_c, mode, size, sigma, epsilon)
    # following will not work, strange design of numpy
    # force[right] -= forcelist
    # force[left] += forcelist
    for i in range(len(forcelist)):
        force[left[i]] += forcelist[i]
        force[right[i]] -= forcelist[i]
    return force


# print(calc_system_force(
#     np.array([[0, 0], [0.01, 0.01]], dtype=float), mode='periodic', r_c=2.5, size=10))
