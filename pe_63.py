import numpy as np
import timeit
import math
import itertools
import pehelperfunctions

def pe_63():
    count = 0
    for i in np.arange(1,10):
        t = 1/(1-math.log10(i))
        count = count + int(t)
    return(count)

if __name__ == '__main__':
    start = timeit.default_timer()
    res = pe_61()
    end = timeit.default_timer()
    print("Result: " + str(res))
    print("Time: " + str(end-start))