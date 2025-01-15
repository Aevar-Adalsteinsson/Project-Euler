import numpy as np
import timeit
import math
import itertools
import pehelperfunctions

def pe_25(n):
    fib_1 = 1
    fib_2 = 1
    fib_n = 2
    while int(math.log10(fib_2))+1 < n:
        temp = fib_1 + fib_2
        fib_1 = fib_2
        fib_2 = temp
        fib_n = fib_n + 1
    return(fib_n)

if __name__ == '__main__':
    start = timeit.default_timer()
    res = pe_25(1000)
    end = timeit.default_timer()
    print("Result: " + str(res))
    print("Time: " + str(end-start))