import numpy as np
import timeit
import math
import itertools
import pehelperfunctions

def pe_50(n):
    primes = pehelperfunctions.gen_primes(n)
    primes_n = len(primes)

    con_p_sum = np.zeros(n+1,dtype = int)
    p_ind = 0
    max_con = 0
    max_p = 0
    for i in np.arange(primes_n):
        p = primes[primes_n-1-i]
        con_sum = 0
        con_n = 0
        p_ind = 0
        while con_sum < p:
            con_sum += primes[p_ind]
            p_ind += 1
            con_n += 1
        if con_n < max_con:
            return(max_p)
        high_ind = p_ind
        low_ind = 0
        while con_sum != p and con_n > max_con:
            if con_sum > p:
                con_sum = con_sum - primes[low_ind]
                con_n = con_n -1
                low_ind += 1
            else:
                con_sum = con_sum + primes[high_ind]
                con_n = con_n +1
                high_ind +=1
        if con_sum == p:
            if con_n > max_con:
                max_con = con_n
                max_p = p
    return(max_p)

if __name__ == '__main__':
    start = timeit.default_timer()
    res = pe_50(1000000)
    end = timeit.default_timer()
    print("Result: " + str(res))
    print("Time: " + str(end-start))