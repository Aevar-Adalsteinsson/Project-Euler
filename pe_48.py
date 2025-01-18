import numpy as np
import timeit
import math
import itertools
import pehelperfunctions

def pe_48(n):
    digits = np.zeros(10,dtype = int)
    for i in np.arange(1,n+1):
        i_digits = np.zeros(10,dtype = int)
        ind = 9
        k = i
        while k > 0 and ind >= 0:
            i_digits[ind] = k%10
            k = k//10
            ind -= 1
        for j in np.arange(i-1):
            i_digits = i_digits*i
            carry = 0
            for l in np.arange(10):
                i_digits[9-l] = i_digits[9-l] + carry
                carry = i_digits[9-l]//10
                i_digits[9-l] = i_digits[9-l]%10
        digits = digits + i_digits
    carry = 0
    for l in np.arange(10):
        digits[9-l] = digits[9-l] + carry
        carry = digits[9-l]//10
        digits[9-l] = digits[9-l]%10
    s = ""
    for digit in digits:
        s = s + str(digit)
    return(s)

if __name__ == '__main__':
    start = timeit.default_timer()
    res = pe_48(1000)
    end = timeit.default_timer()
    print("Result: " + str(res))
    print("Time: " + str(end-start))