import numpy as np
import timeit
import math
import itertools
import pehelperfunctions

def pe_20(n):
    log_sum = 0
    for i in range(2,n+1):
        log_sum = log_sum + math.log10(i)
    n_dig = int(log_sum) + 1
    digits = np.zeros(n_dig)
    digits[0] = 1
    max_dig = 1
    for i in range(2,n+1):
        digits[:max_dig] = i*digits[:max_dig]
        carry = 0
        for j in range(max_dig):
            total = carry + digits[j]
            carry = total//10
            digits[j] = total%10
        while carry > 0:
            max_dig = max_dig + 1
            digits[max_dig-1] = carry%10
            carry = carry//10
    return(np.sum(digits))

if __name__ == '__main__':
    start = timeit.default_timer()
    res = pe_20(100)
    end = timeit.default_timer()
    print("Result: " + str(res))
    print("Time: " + str(end-start))