import numpy as np
import timeit
import math
import itertools
import pehelperfunctions

def pe_35(n):
    primes = pehelperfunctions.gen_primes(n)
    n_primes = len(primes)
    max_digits = int(math.log10(primes[len(primes)-1])) + 1
    digits = np.zeros(max_digits,dtype=int)
    circ_dict = {2:True,3:True,5:True,7:True}
    n_circ = 4
    for p in primes[4:]:
        p_ndig = int(math.log10(p)) + 1
        p_dig, p_ind = pehelperfunctions.get_digits(digits[:p_ndig],p)
        flag = False
        for digit in p_dig:
            if digit%2 == 0 or digit == 5:
                flag = True
                break
        if flag:
            continue
        flag = False
        
        circ_cand = np.zeros(p_ndig)
        circ_cand[0] = p
        min_circ = math.inf
        for i in range(1,p_ndig):
            p_cand = 0
            for j in range(p_ndig):
                p_cand = p_cand + p_dig[(j+i)%p_ndig]*(10**j)
            min_circ = min(min_circ,p_cand)
            circ_cand[i] = p_cand
            if not pehelperfunctions.bin_search_check(primes,p_cand,0,n_primes):
                flag = True
                break
        if flag:
            continue
        if min_circ not in circ_dict:
            for circ in circ_cand:
                circ_dict[circ] = True
    return(len(circ_dict))

if __name__ == '__main__':
    start = timeit.default_timer()
    res = pe_35(1000000)
    end = timeit.default_timer()
    print("Result: " + str(res))
    print("Time: " + str(end-start))