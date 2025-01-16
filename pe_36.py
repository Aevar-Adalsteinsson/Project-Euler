import numpy as np
import timeit
import math
import itertools
import pehelperfunctions

def pe_36(n):
    pal_sum = 0
    for i in np.arange(1,n):
        if pehelperfunctions.is_palindrome(i):
            bin_str = bin(i)[2:]
            if pehelperfunctions.is_palindrome_str(bin_str):
                pal_sum = pal_sum + i
                #print(i)
    return(pal_sum)

if __name__ == '__main__':
    start = timeit.default_timer()
    res = pe_36(1000000)
    end = timeit.default_timer()
    print("Result: " + str(res))
    print("Time: " + str(end-start))