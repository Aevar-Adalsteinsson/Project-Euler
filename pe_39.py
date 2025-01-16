import numpy as np
import timeit
import math
import itertools
import pehelperfunctions

def pe_39(n):
    int_tri_max = 0
    max_i = 0
    for i in np.arange(6,n+1):
        pyth_n = 0
        for a in np.arange(1,i//3):
            r = i-a
            b = (r**2-a**2)/(2*r)
            c = r-b
            if b == int(b):
                pyth_n = pyth_n + 1
        if pyth_n > int_tri_max:
            int_tri_max = pyth_n
            max_i = i
    return(max_i)

if __name__ == '__main__':
    start = timeit.default_timer()
    res = pe_39(1000)
    end = timeit.default_timer()
    print("Result: " + str(res))
    print("Time: " + str(end-start))