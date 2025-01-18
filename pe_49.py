import numpy as np
import timeit
import math
import itertools
import pehelperfunctions

def pe_49():
    primes = pehelperfunctions.gen_primes(10000)
    ind = np.searchsorted(primes,1000)
    primes = primes[ind:]
    prime_n = len(primes)
    for i in np.arange(prime_n-3):
        p_1 = primes[i]
        digits = pehelperfunctions.get_digits_2(p_1)
        digits = np.sort(digits)
        for j in np.arange(i+1,prime_n-2):
            arith_n = 2
            p_2 = primes[j]
            digits_j = np.sort(pehelperfunctions.get_digits_2(p_2))
            inc = p_2 - p_1
            arith_concat = str(p_1) + str(p_2)
            if (digits_j == digits).all():
                p_curr = p_2
                while arith_n < 3:
                    
                    p_curr = p_curr + inc
                    digits_curr = np.sort(pehelperfunctions.get_digits_2(p_curr))
                    prime_ind = np.searchsorted(primes,p_curr)
                    if p_curr < 10000 and (digits_curr == digits).all() and p_curr == primes[prime_ind]:
                        arith_n = arith_n + 1
                        arith_concat = arith_concat + str(p_curr)
                    else:
                        break
                if arith_n == 3:
                    if p_1 == 1487:
                        continue
                    return(arith_concat)

if __name__ == '__main__':
    start = timeit.default_timer()
    res = pe_49()
    end = timeit.default_timer()
    print("Result: " + str(res))
    print("Time: " + str(end-start))