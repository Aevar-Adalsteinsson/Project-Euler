import numpy as np
import timeit
import math
import itertools
import pehelperfunctions

def pe_29(n):
    nums = np.arange(2,n+1)
    distinct_powers = 0
    for i in range(len(nums)):
        powers = np.zeros(0,dtype = int)
        power = nums[i]
        if power > 0:
            curr_power = power
            exponent_power = 1
            while curr_power < n+1:
                nums[curr_power-2] = 0
                powers = np.append(powers,exponent_power*np.arange(2,n+1))
                curr_power = curr_power*power
                exponent_power = exponent_power + 1
            powers.sort()
            distinct_powers = distinct_powers + 1
            for i in range(1,len(powers)):
                if powers[i-1] != powers[i]:
                    distinct_powers = distinct_powers + 1
    return(distinct_powers)

if __name__ == '__main__':
    start = timeit.default_timer()
    res = pe_29(100)
    end = timeit.default_timer()
    print("Result: " + str(res))
    print("Time: " + str(end-start))