import numpy as np
import timeit
import math
import itertools
import pehelperfunctions

def pe_6(n):
    nums = np.arange(1,n+1)
    nums_sum = n*(n+1)/2
    nums_sq = nums ** 2
    return(nums_sum**2 - np.sum(nums_sq))

if __name__ == '__main__':
    start = timeit.default_timer()
    res = pe_6(100)
    end = timeit.default_timer()
    print("Result: " + str(res))
    print("Time: " + str(end-start))