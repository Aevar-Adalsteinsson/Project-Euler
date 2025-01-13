import numpy as np
import timeit
import math
import itertools
import pehelperfunctions

def pe_9(n):
    a_upper = n//3 - 1
    for a in range(1,a_upper+1):
        if (n-a)%2 == 0:
            b_upper = (n-a)/2 - 1
        else:
            b_upper = (n-a)//2
        b_upper = (n-a)
        b = np.arange(a+1,b_upper+1)
        c = n - b - a
        pyth_ab = a**2 + b**2
        pyth_c = c**2
        index = np.where((pyth_ab - pyth_c) == 0)
        if index[0].size == 1:
            b = b[index[0]][0]
            c = c[index[0]][0]
            return(a*b*c)

if __name__ == '__main__':
    start = timeit.default_timer()
    res = pe_9(1000)
    end = timeit.default_timer()
    print("Result: " + str(res))
    print("Time: " + str(end-start))