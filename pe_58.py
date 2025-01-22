import numpy as np
import timeit
import math
import itertools
import pehelperfunctions

def pe_58():
    n = 10**3
    primes = pehelperfunctions.gen_primes(n)

    total = 1
    n_p = 0
    m = 1
    while True:
        p_1 = 2*m*(2*m+1) + 1
        p_2 = (2*m+1)**2
        p_3 = (2*m)**2+1
        p_4 = (2*m)*(2*m-1) + 1
        
        if pehelperfunctions.is_prime(primes,p_1):
            n_p = n_p + 1
        if pehelperfunctions.is_prime(primes,p_3):
            n_p = n_p + 1
        if pehelperfunctions.is_prime(primes,p_4):
            n_p = n_p + 1
        total = total+4
        if n_p/total < 0.1:
            return(2*m+1)
        m = m+1

if __name__ == '__main__':
    start = timeit.default_timer()
    res = pe_58()
    end = timeit.default_timer()
    print("Result: " + str(res))
    print("Time: " + str(end-start))