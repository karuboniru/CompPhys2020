import numpy as np


def generate_indices(n, i):
    left = [i for k in range(n-1)]
    right = [(k < i)*k + (k >= i)*(k+1) for k in range(n-1)]
    return left, right


def calc_force(r, r_c, mode, size, sigma, epsilon):
    if mode == 'periodic':
        np.add(r, size/2, out=r)
        np.mod(r, size, out=r)
        np.add(r, -size/2, out=r)
    nr = np.linalg.norm(r)
    if(nr >= r_c):
        return np.array(np.zeros_like(r))
    return 4*epsilon*(12*sigma**12/nr**14 - 6*sigma**6/nr**8)*r


def calc_total_force(x, mode, size=None, sigma=1.0, epsilon=1.0, r_c=2.5):
    n, _ = np.shape(x)
    force = np.empty_like(x)
    for i in range(n):
        left, right = generate_indices(n, i)
        force[i] += np.sum(calc_force(r=x[left] - x[right], r_c=r_c, mode=mode,
                                      size=size, sigma=sigma, epsilon=epsilon), axis=1)
    return force