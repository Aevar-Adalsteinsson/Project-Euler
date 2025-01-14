import numpy as np
import timeit
import math
import itertools
import pehelperfunctions


def pe_15(n_1,m_1):
    n = n_1 + 1
    m = m_1 + 1
    latt_n = np.zeros((n,m))
    latt_n[0,1:] = np.ones(m-1)
    for i in range(1,n):
        for j in range(i,m):
            if i == j:
                latt_n[i,j] = 2*latt_n[i-1,j]
            else:
                latt_n[i,j] = latt_n[i-1,j] + latt_n[i,j-1]
    return(latt_n[n-1,m-1])

if __name__ == '__main__':
    start = timeit.default_timer()
    res = pe_15(20,20)
    end = timeit.default_timer()
    print("Result: " + str(res))
    print("Time: " + str(end-start))