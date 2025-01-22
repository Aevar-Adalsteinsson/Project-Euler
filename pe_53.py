import numpy as np
import timeit
import math
import itertools
import pehelperfunctions

def pe_53():
    m = 100
    log_n = np.log(np.arange(1,m+1))
    log_fact_n = np.zeros(m+1)
    for i in np.arange(1,m+1):
        log_fact_n[i] = log_fact_n[i-1]+log_n[i-1]
    mill_log = np.log(10**6)
    count = 0
    for n in np.arange(1,m+1):
        for r in np.arange(n):#it is possible to reduce the number by half by use of symmetry
            log_fact = log_fact_n[n]-log_fact_n[r]-log_fact_n[n-r]
            if log_fact>mill_log:
                count = count + 1
    return(count)

if __name__ == '__main__':
    start = timeit.default_timer()
    res = pe_53()
    end = timeit.default_timer()
    print("Result: " + str(res))
    print("Time: " + str(end-start))