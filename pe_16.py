import numpy as np
import timeit
import math
import itertools
import pehelperfunctions


def pe_16(n):
    n_dig = int(n*np.log10(2)) + 1
    digits = np.zeros(n_dig)
    digits[0] = 1
    high_dig = 1
    for i in range(n):
        digits[0:high_dig] = digits[0:high_dig]*2
        carry = 0
        for j in range(high_dig):
            numb = carry + digits[j]
            digits[j] = numb%10
            carry = numb//10
        if carry > 0:
            high_dig = high_dig + 1
            digits[high_dig-1] = carry
    return(np.sum(digits))

if __name__ == '__main__':
    start = timeit.default_timer()
    res = pe_16(1000)
    end = timeit.default_timer()
    print("Result: " + str(res))
    print("Time: " + str(end-start))