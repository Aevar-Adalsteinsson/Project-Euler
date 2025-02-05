import numpy as np
import timeit
import math
import itertools
import pehelperfunctions

def pe_71(d):
    primes = pehelperfunctions.gen_primes(d)
    val = d//7
    upper = 3*val
    for i in range(upper,0,-1):
        if np.gcd(i,7*val) == 1:
            closest = 3/7-i/(7*val)#good candidate
            closest_nd = (i,7*val)
            break

    for i in range(2,d+1):
        if i == 7:
            continue
        
        upper = i*3//7 
        if 3/7-upper/i > closest:
            continue
        i_div = pehelperfunctions.get_prime_divisor_simple(i,primes)
        for j in range(upper,0,-1):
            diff = 3/7-j/i
            if diff > closest:
                break
            is_coprime = True
            for prime in i_div:
                if j%prime == 0:
                    is_coprime = False
                    break
            if is_coprime:
                if diff < closest:
                    closest = diff
                    closest_nd = (j,i)
                break
    return(closest_nd[0])

if __name__ == '__main__':
    start = timeit.default_timer()
    res = pe_71(1000000)
    end = timeit.default_timer()
    print("Result: " + str(res))
    print("Time: " + str(end-start))