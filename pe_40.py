import numpy as np
import timeit
import math
import itertools
import pehelperfunctions

def pe_40():
    def get_dec_digit(n):
        if n < 10:
            return(n)
        n = n - 10
        dig = 2
        while True:
            tot_dig = dig*9*(10**(dig-1))
            if tot_dig > n:
                break
            n = n-tot_dig
            dig = dig + 1
        quot = n//dig
        rem = n%dig
    
        num = 10**(dig-1) + quot
        digit = num//10**(dig-1-rem)
        digit = digit%10
        return(digit)
    digs = 10**np.arange(7)
    prod = 1
    for dig in digs:
        prod = prod*get_dec_digit(dig)
    return(prod)

if __name__ == '__main__':
    start = timeit.default_timer()
    res = pe_40()
    end = timeit.default_timer()
    print("Result: " + str(res))
    print("Time: " + str(end-start))