import numpy as np
import timeit
import math
import itertools
import pehelperfunctions


def pe_10(n):
    primes = pehelperfunctions.gen_primes(n)
    return(np.sum(primes,dtype = np.int64))

if __name__ == '__main__':
    start = timeit.default_timer()
    res = pe_10(2000000)
    end = timeit.default_timer()
    print("Result: " + str(res))
    print("Time: " + str(end-start))