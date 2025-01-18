import numpy as np
import timeit
import math
import itertools
import pehelperfunctions

def pe_43():
    def digits_next(digits,ind):
        dig_sort = np.sort(digits[ind:])
        dig_sort = np.flip(dig_sort)
        digits = np.append(digits[:ind],dig_sort)
        digits = pehelperfunctions.next_pandigital(digits,len(digits))
        return(digits)
    pan_sum = 0.0
    digits = np.array([1,0,2,3,4,5,6,7,8,9],dtype = float)
    primes = np.array([2,3,5,7,11,13,17])
    highest = np.array([9,8,7,6,5,4,3,2,1,0],dtype = float)
    count = 0
    while not (highest == digits).all():
        flag = False
        for i in np.arange(7):
            ind = i+1
            num = digits[ind]*100 + digits[ind+1]*10 + digits[ind+2]
            if num%primes[i] != 0:
                digits = digits_next(digits,i+4)
                flag = True
                break
        if flag:
            continue
        pan_sum = pan_sum + np.sum(10**np.arange(10-1,-1,-1)*digits)
        digits = pehelperfunctions.next_pandigital(digits,len(digits))
    return(pan_sum)

if __name__ == '__main__':
    start = timeit.default_timer()
    res = pe_43()
    end = timeit.default_timer()
    print("Result: " + str(res))
    print("Time: " + str(end-start))