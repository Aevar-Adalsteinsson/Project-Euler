import numpy as np
import timeit
import math
import itertools

def pe_1(p1,p2,n):
#https://projecteuler.net/problem=1
    if(p1%p2 == 0):
        return(sum(range(p2,n,p2)))
    if(p2%p1 == 0):
        return(sum(range(p1,n,p1)))
    factor_sum = sum(range(p1,n,p1)) + sum(range(p2,n,p2)) - sum(range(p1*p2,n,p1*p2)) 
    return(factor_sum)

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
    completed = [1,2]
    inputs = {1:(3,5,1000),2:(4000000,)}
    for i in completed:
        pe_func = "pe_" + str(i)
        args = inputs[i]
        exec(f"x = {pe_func}")

        start = timeit.default_timer()
        res = x(*args)
        end = timeit.default_timer()
        print("Result: " + str(res))
        print("Time: " + str(end-start))