import numpy as np
import timeit
import math
import itertools
import pehelperfunctions

def pe_47():
    distinct_n = 0
    n = 4
    primes = [2,3,5,7]
    next_prime = 5
    next_prime_ind = 2
    primes_ind = {2:0,3:1}
    max_prime = primes[len(primes)-1]
    while distinct_n < 4:
        if next_prime - (n-1) + distinct_n <= 3:
            distinct_n = 0
            n = next_prime + 1
            prev_prime = next_prime
            next_prime_ind += 1
            next_prime = primes[next_prime_ind]
            while next_prime - prev_prime < 5:
                if next_prime >= max_prime:
                    primes, primes_ind = pehelperfunctions.gen_additional_primes(n*5,primes,primes_ind)#5 arbitrarily chosen
                    max_prime = primes[len(primes)-1]
                n = next_prime+1
                prev_prime = next_prime
                next_prime_ind += 1
                next_prime = primes[next_prime_ind]
                
            if next_prime >= max_prime:
                primes, primes_ind = pehelperfunctions.gen_additional_primes(n*5,primes,primes_ind)#5 arbitrarily chosen
                max_prime = primes[len(primes)-1]
        if max_prime < n:
            primes, primes_ind = pehelperfunctions.gen_additional_primes(n*5,primes,primes_ind)#5 arbitrarily chosen
            max_prime = primes[len(primes)-1]
        prime_div_n = pehelperfunctions.get_prime_divisor_n(n,primes[:(next_prime_ind+1)])
        if prime_div_n >= 4:
            distinct_n += 1
        else:
            distinct_n = 0
        n = n+1
    return(n-4)

if __name__ == '__main__':
    start = timeit.default_timer()
    res = pe_47()
    end = timeit.default_timer()
    print("Result: " + str(res))
    print("Time: " + str(end-start))