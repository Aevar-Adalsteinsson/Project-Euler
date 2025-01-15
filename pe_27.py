import numpy as np
import timeit
import math
import itertools
import pehelperfunctions

def pe_27(n,m):
    # n^2 + an + b
    # |a|<n, |b|<= m
    primes = pehelperfunctions.gen_primes(m)
    max_prime = primes[len(primes)-1]
    primes_n = len(primes)
    max_chain = 0
    for b in primes:
        for a in range(-b+1,n):
            n = 1
            chain_n = 1
            prime_cand = n**2 + a*n + b
            if prime_cand < prime_cand:
                primes = pehelperfunctions.gen_additional_primes_2(max_prime*5,primes)#5 arbitrary
                primes_n = len(primes)
                max_primes = primes[primes_n-1]
            while prime_cand in primes:#could be improved
                chain_n = chain_n +1
                n = n+1
                prime_cand = n**2 + a*n + b#could be +a -1 + 2n, (n-1)(n-1) = n^2 -2n+1
                if prime_cand < prime_cand:
                    primes = pehelperfunctions.gen_additional_primes_2(max_prime*5,primes)#5 arbitrary
                    primes_n = len(primes)
                    max_primes = primes[primes_n-1]
            if chain_n > max_chain:
                max_pair = a*b
                max_chain = chain_n
    return(max_pair)

if __name__ == '__main__':
    start = timeit.default_timer()
    res = pe_27(1000,1000)
    end = timeit.default_timer()
    print("Result: " + str(res))
    print("Time: " + str(end-start))