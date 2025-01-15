import numpy as np
import timeit
import math
import itertools
import pehelperfunctions

def pe_30():
    power_sum = 0
    for i in range(2,354294):
        digit_sum = 0
        i_og = i
        rem = i%10
        i = i//10
        while i > 0:
            digit_sum = digit_sum + rem**5
            rem = i%10
            i = i//10
        digit_sum = digit_sum + rem**5
        if digit_sum == i_og:
            power_sum = power_sum + i_og
    return(power_sum)

if __name__ == '__main__':
    start = timeit.default_timer()
    res = pe_30()
    end = timeit.default_timer()
    print("Result: " + str(res))
    print("Time: " + str(end-start))