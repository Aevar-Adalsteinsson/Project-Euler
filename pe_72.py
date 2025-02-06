import numpy as np
import timeit
import math
import itertools
import pehelperfunctions

def pe_72(d):
    #need nested loop because we overcount non reduce proper fraction by simply going through the primes
    #example: we overcount 6/30 since 2 and 3 is both factors of 6
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
    
    
    all_frac = (d-1)*d//2
    primes = pehelperfunctions.gen_primes(d//2 + 1)
    non_red = 0
    
    prime_m = nested_loop([],primes,[],d)
    for i in range(len(prime_m)):
        prime_factors = prime_m[i]
        num = math.prod(prime_factors)
        if len(prime_factors)%2 == 1:
            pm = 1
        else:
            pm = -1
        k = d//int(num)-1          #numbers n <= d that satisfy gcd(n,num) = num^s for some s > 0 excluding p itself
        non_red += pm*k*(k+1)//2   #each multiple of p, say np, has n-1 non reduced fraction because of p 

    return(all_frac-non_red)

if __name__ == '__main__':
    start = timeit.default_timer()
    res = pe_72(10**6)
    end = timeit.default_timer()
    print("Result: " + str(res))
    print("Time: " + str(end-start))