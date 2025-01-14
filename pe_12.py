import numpy as np
import timeit
import math
import itertools
import pehelperfunctions


def pe_12(n):
    m = 2
    primes = np.array([2,3])
    primes_ind = {2:0,3:1}
    primes_up_to = 3
    prev_divisors = np.array([0,1])
    while True:
        tri = m*(m+1)/2
        if m+1 > primes_up_to:
            old_len = len(primes)
            primes, primes_ind = pehelperfunctions.gen_additional_primes(10*primes_up_to,primes,primes_ind)
            primes_up_to = 10*primes_up_to
            new_len = len(primes)
            prev_divisors = np.append(prev_divisors,np.zeros(new_len-old_len))
        if m%2 == 0:
            divisors_2 = pehelperfunctions.get_prime_divisors(m+1,primes,primes_ind)
        else:
            divisors_2 = pehelperfunctions.get_prime_divisors((m+1)/2,primes,primes_ind)
        divisors_1 = prev_divisors
        prev_divisors = divisors_2
        divisors = divisors_1 + divisors_2
        factors = np.prod(divisors+1)
        if factors > n:
                return(tri)
        m = m+1


if __name__ == '__main__':
    start = timeit.default_timer()
    res = pe_12(500)
    end = timeit.default_timer()
    print("Result: " + str(res))
    print("Time: " + str(end-start))