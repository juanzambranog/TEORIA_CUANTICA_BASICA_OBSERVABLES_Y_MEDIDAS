import numpy as np


def probabilidad_pos(v, p):
    norma = np.linalg.norm(v) ** 2
    c = (abs(v[p]))**2
    return c/norma

def probabilidad_transitar(v, k):

    nv = np.linalg.norm(v)
    nk = np.linalg.norm(k)
    for i in range(len(v)):
        v[i] = v[i] / nv
        k[i] = k[i] / nk

    prod_in = 0
    for i in range(len(v)):
        prod_in+=k[i]*v[i]

    prod_v = nv * nk
    prob = prod_in / prod_v
    return prob


print(probabilidad_pos([-3-1j,-2j,1j,2],2))

print(probabilidad_transitar([1,2,3,4,2],[9,1,8,7,6]))