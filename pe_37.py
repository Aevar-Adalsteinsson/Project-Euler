import numpy as np
import timeit
import math
import itertools
import pehelperfunctions

def pe_37():
    n = 1000000
    primes = pehelperfunctions.gen_primes(n)
    dig1_primes = [2,3,5,7]
    trunc_sum = 0
    for p in primes[4:]:
        p_n = int(math.log10(p))+1
        digits = pehelperfunctions.get_digits_2(p)
        
        if digits[0] not in dig1_primes:
            continue
        if digits[p_n-1] not in dig1_primes[1:]:
            continue
        flag = False
        for i in np.arange(1,p_n-1):
            if digits[i]%2 == 0:
                flag = True
                break
        if flag:
            continue
        p_left = p
        p_right = p
        for i in np.arange(p_n-1):
            p_left = p_left % 10**(p_n-i-1)
            p_right = p_right//10
            if p_left not in primes or p_right not in primes:
                flag = True
                break
        if flag:
            continue
        trunc_sum = trunc_sum + p
    return(trunc_sum)

if __name__ == '__main__':
    start = timeit.default_timer()
    res = pe_37()
    end = timeit.default_timer()
    print("Result: " + str(res))
    print("Time: " + str(end-start))