import numpy as np
import timeit
import math
import itertools
import pehelperfunctions

def pe_23():
    n = 28123
    primes = pehelperfunctions.gen_primes(n+1)
    n_p = len(primes)
    div_sum = np.zeros(n,dtype = int)
    divisors = np.zeros(n_p,dtype = int)
    for i in range(2,n+1):
        cand = i
        prime_index = 0
        while cand != 1:
            prime = primes[prime_index]
            while cand%prime == 0:
                cand = cand//prime
                divisors[prime_index] = divisors[prime_index] + 1
            prime_index = prime_index + 1
        pos_index = np.where(divisors>0)
        divisors_pos = divisors[pos_index]
        prime_key = primes[pos_index]
        div_sum[i-1] = pehelperfunctions.divisor_sum(divisors_pos,prime_key,i)
        divisors[:prime_index] = np.zeros(prime_index,dtype = int)
    abun_index = np.where((div_sum-np.arange(1,n+1))>0)
    abun = np.arange(1,n+1)[abun_index]
    abun_sum = np.arange(1,n+1)
    for i in abun:
        for j in abun:
            if i + j <= n:
                abun_sum[i+j-1] = 0
    return(np.sum(abun_sum))

if __name__ == '__main__':
    start = timeit.default_timer()
    res = pe_23()
    end = timeit.default_timer()
    print("Result: " + str(res))
    print("Time: " + str(end-start))