import numpy as np
import timeit
import math
import itertools
import pehelperfunctions

def pe_31(coins,amount):
    #every coin must be a multiple of last coin
    #coins and amount must be integers
    #coins in increasing order
    n = len(coins)
    if n == 1:
        return(1)
    if n == 2:
        return(amount//coins[1] + 1)
    coin = coins[n-1]
    sums = 0
    for i in range(amount//coin+1):
        sums_i = pe_31(coins[:(n-1)],amount-i*coin)
        sums = sums + sums_i
    return(sums)

if __name__ == '__main__':
    start = timeit.default_timer()
    res = pe_31([1,2,5,10,20,50,100,200],200)
    end = timeit.default_timer()
    print("Result: " + str(res))
    print("Time: " + str(end-start))