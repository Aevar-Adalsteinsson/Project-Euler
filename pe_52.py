import numpy as np
import timeit
import math
import itertools
import pehelperfunctions

def pe_52():
    for i in np.arange(3,7):
        for j in np.arange(10**i,10**(i+1)//6+1):
            j_digits = pehelperfunctions.get_digits_2(j)
            j_digits.sort()
            flag = True
            for k in np.arange(2,7):
                digits = pehelperfunctions.get_digits_2(k*j)
                digits.sort()
                if not all(j_digits == digits):
                    flag = False
                    break
            if flag:
                return(j)

if __name__ == '__main__':
    start = timeit.default_timer()
    res = pe_52()
    end = timeit.default_timer()
    print("Result: " + str(res))
    print("Time: " + str(end-start))