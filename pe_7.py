import numpy as np
import timeit
import math
import itertools
import pehelperfunctions

def pe_7(n):
    upper = n*(np.log(n) + np.log(np.log(n)))
    primes = pehelperfunctions.gen_primes(int(upper))
    return(primes[n-1])

if __name__ == '__main__':
    start = timeit.default_timer()
    res = pe_7(10001)
    end = timeit.default_timer()
    print("Result: " + str(res))
    print("Time: " + str(end-start))