import numpy as np
import timeit
import math
import itertools

def pe_2(n):
    fib_even = 0
    fib = 2   # fib n
    fib_p = 1 # fib n-1
    while fib<n:
        fib_even = fib_even + fib
        fib_temp = fib + fib_p #odd fib n+1
        fib_p = fib + fib_temp #odd fib n+2
        fib = fib_temp + fib_p #even fib n+3 => fib n
    return(fib_even)

if __name__ == '__main__':
    start = timeit.default_timer()
    res = pe_2(4000000)
    end = timeit.default_timer()
    print("Result: " + str(res))
    print("Time: " + str(end-start))