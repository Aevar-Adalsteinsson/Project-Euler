import numpy as np
import timeit
import math
import itertools
import pehelperfunctions

def pe_69(n):
    primes = pehelperfunctions.gen_primes(n)
    primes_n = len(primes)
    max_tot = 1
    max_tot_n = 1
    total = 2
    prime_div = [2]
    i = 0
    while total <= n:
        tot = pehelperfunctions.totient(prime_div,total)
        if total/tot > max_tot:
            max_tot = total/tot
            max_tot_n = total
        i += 1
        p = primes[i]
        total = total*p
        prime_div.append(p)
    return(max_tot_n)

if __name__ == '__main__':
    start = timeit.default_timer()
    res = pe_69(1000000)
    end = timeit.default_timer()
    print("Result: " + str(res))
    print("Time: " + str(end-start))