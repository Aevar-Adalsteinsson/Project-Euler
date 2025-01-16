import numpy as np
import timeit
import math
import itertools
import pehelperfunctions

def pe_38():
    #9(1,2,3,4,5) = 918273645 exists so the leading digit must be 9
    pandig_max = 918273645
    for i in np.arange(2,5):
        #i number of digit
        for n in np.arange(9*(10**i)+1,10**(i+1)):
            digits = pehelperfunctions.get_digits_2(n)
            if 0 in digits:
                continue
            if len(digits) != len(set(digits)):
                continue
            s = ""#
            mult_ind = 1
            while len(s)<9:
                s = s + str(n*mult_ind)
                mult_ind = mult_ind + 1
            s_len = len(s)
            if s_len != 9 or "0" in s or s_len != len(set(s)):
                continue
            m = int(s)
            if m > pandig_max:
                pandig_max = m
    return(pandig_max)

if __name__ == '__main__':
    start = timeit.default_timer()
    res = pe_38()
    end = timeit.default_timer()
    print("Result: " + str(res))
    print("Time: " + str(end-start))