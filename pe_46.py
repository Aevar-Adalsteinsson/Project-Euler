import numpy as np
import timeit
import math
import itertools
import pehelperfunctions

def pe_46():
    primes = pehelperfunctions.gen_primes(100000)
    p_n = len(primes)
    n = 35
    while True:
        if n in primes:
            n = n+2
            continue
        ind = 0
        flag = False
        while ind < p_n:
            p = primes[ind]
            if p >= n:
                break
            square = (n-p)/2
            if np.sqrt(square).is_integer():
                flag = True
                break
            ind = ind + 1
        if flag:
            n = n+2
            continue
        return(n)

if __name__ == '__main__':
    start = timeit.default_timer()
    res = pe_46()
    end = timeit.default_timer()
    print("Result: " + str(res))
    print("Time: " + str(end-start))