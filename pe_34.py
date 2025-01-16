import numpy as np
import timeit
import math
import itertools
import pehelperfunctions

def pe_34():
    fact_digit_sum = 0
    digits = np.zeros(7,dtype = int)
    for i in range(10,2540160):
        i_digs,i_index = pehelperfunctions.get_digits(digits,i)
        vfunc = np.vectorize(math.factorial)
        fact_sum = np.sum(vfunc(i_digs[:i_index]))
        if i == fact_sum:
            fact_digit_sum = fact_digit_sum + i
    return(fact_digit_sum)

if __name__ == '__main__':
    start = timeit.default_timer()
    res = pe_34()
    end = timeit.default_timer()
    print("Result: " + str(res))
    print("Time: " + str(end-start))