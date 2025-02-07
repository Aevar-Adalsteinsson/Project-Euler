import numpy as np
import timeit
import math
import itertools
import pehelperfunctions

def pe_73(d):
    def nested_loop(prime_m,primes,factors,n):
        if len(factors)>0:
            prime_m.append(factors)
        if len(primes) == 0 or n < primes[0]:
            return(prime_m)
        
        for i in range(len(primes)):
            p = primes[i]
            k = n//int(p)-1
            #if len(factors) == 0:
            #    k = k-1
            if k == 0:
                break
            new_factors = [x for x in factors]
            new_factors.append(p)
            prime_m = nested_loop(prime_m,primes[(i+1):],new_factors,n//p)
        return(prime_m)
    all_frac = 0
    frac_n = 0
    primes = pehelperfunctions.gen_primes(d)
    for i in range(5,d+1):
        prime_factors = pehelperfunctions.get_prime_divisor_simple(i,primes)
        factors_i = nested_loop([],prime_factors,[],i)
        lower = i//3 + 1 #i/3 < lower
        if i%2 == 0:
            upper = i//2
        else:
            upper = i//2 + 1
        if lower < upper:
            all_frac += upper-lower
        else:
            continue
        
        for factor in factors_i:
            num = math.prod(factor)
            if len(factor)%2 == 1:
                pm = 1
            else:
                pm = -1
            num_low = lower//num
            if lower%num == 0:
                frac_n += pm
            f_range = upper - lower - 1 + lower%num
            if f_range < num:
                continue
            frac_n += pm*(f_range//num)
    return(all_frac-frac_n)

if __name__ == '__main__':
    start = timeit.default_timer()
    res = pe_73(12000)
    end = timeit.default_timer()
    print("Result: " + str(res))
    print("Time: " + str(end-start))