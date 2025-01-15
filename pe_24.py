import numpy as np
import timeit
import math
import itertools
import pehelperfunctions

def pe_24(n,m):
    #only works for small n and m
    perm = np.zeros(m,dtype = int)
    rank_rem = n-1
    nums = np.arange(m)
    for i in range(m):
        fact_i = math.factorial(m-1-i)
        quotient = rank_rem//fact_i
        rank_rem = rank_rem%fact_i
        perm[i] = nums[quotient]
        nums = np.delete(nums,quotient)
    s = ""
    for p in perm:
        s = s + str(p)
    return(s)

if __name__ == '__main__':
    start = timeit.default_timer()
    res = pe_24(1000000,10)
    end = timeit.default_timer()
    print("Result: " + str(res))
    print("Time: " + str(end-start))