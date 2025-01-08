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


if __name__ == '__main__':
    start = timeit.default_timer()
    res = pe_1(3,5,1000)
    end = timeit.default_timer()
    print("Result: " + str(res))
    print("Time: " + str(end-start))