import numpy as np
import timeit
import math
import itertools
import pehelperfunctions

def pe_45():
    n = 144.0
    while True:
        hex_n = n*(2*n-1)
        pent_n = (1+np.sqrt(1+24*hex_n))/6
        if not pent_n.is_integer():
            n = n+1
            continue
        tri_n = (-1+np.sqrt(1+8*hex_n))/2
        if tri_n.is_integer():
            return(hex_n)
        n = n+1
        

if __name__ == '__main__':
    start = timeit.default_timer()
    res = pe_45()
    end = timeit.default_timer()
    print("Result: " + str(res))
    print("Time: " + str(end-start))