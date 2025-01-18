import numpy as np
import timeit
import math
import itertools
import pehelperfunctions

def pe_41():
    for m in np.arange(9,0,-1):
        digits = np.arange(m,0,-1)
        pandig = np.sum(10**np.arange(m-1,-1,-1)*digits)
        n = int(np.sqrt(pandig))+1
        primes = pehelperfunctions.gen_primes(n)
        count = 0
        bound = math.factorial(m)
        while count < bound:
            prev_digits = np.copy(digits)
            digits = pehelperfunctions.prev_pandigital(digits,m)
            diff = np.sum(10**np.arange(m-1,-1,-1)*(digits-prev_digits))
            pandig = pandig + diff
            count = count + 1
            #print(pandig)
            flag = True
            for p in primes:
                if pandig%p == 0:
                    flag = False
                    break
            if flag:
                #print(pandig)
                return(pandig)

if __name__ == '__main__':
    start = timeit.default_timer()
    res = pe_41()
    end = timeit.default_timer()
    print("Result: " + str(res))
    print("Time: " + str(end-start))