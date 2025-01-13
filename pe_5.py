import numpy as np
import timeit
import math
import itertools
import pehelperfunctions

def pe_5(n):
    primes = pehelperfunctions.gen_primes(n)
    f_x = lambda x: int(np.log(n)/np.log(x))
    mapf = np.vectorize(f_x)
    prime_mult = mapf(primes)
    factors = primes ** prime_mult
    return(np.prod(factors))

if __name__ == '__main__':
    start = timeit.default_timer()
    res = pe_5(20)
    end = timeit.default_timer()
    print("Result: " + str(res))
    print("Time: " + str(end-start))