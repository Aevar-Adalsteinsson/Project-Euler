import numpy as np
import timeit
import math
import itertools
import pehelperfunctions

def pe_78(n):
    p_m = [1,1,2,3,5]
    m = 5
    while True:
        m_sum = 0
        i = 1
        while True:
            k = (i-1)//2 + 1
            if i%2 == 0:
                k = k*(-1)
            pent = k*(3*k-1)//2
            if pent > m:
                break
            if (k-1)%2 == 0:
                pm = 1
            else:
                pm = -1
            m_sum = m_sum + pm*p_m[m-pent]
            i += 1
        if m_sum%n == 0:
            return(m)
        p_m.append(m_sum)
        m = m+1


if __name__ == '__main__':
    start = timeit.default_timer()
    res = pe_78(10**6)
    end = timeit.default_timer()
    print("Result: " + str(res))
    print("Time: " + str(end-start))