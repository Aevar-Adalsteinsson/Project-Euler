import numpy as np
import timeit
import math
import itertools
import pehelperfunctions

def pe_77(n):
    primes = pehelperfunctions.gen_primes(10000)
    prev_part = [[0,0,1],[0,0,0],[0,0,0]] #prev_par[i][j] is how many sums of primes less or equal to primes[i] sum up to j
    i = 3
    while True:
        for j in range(len(prev_part)):
            prev_part[j].append(0)
        if primes[len(prev_part)] <= i:
            new_list = [0]*(i+1)
            prev_part.append(new_list)
        
        if i%2 == 0:
            prev_part[0][i] = 1
        for j in range(1,i+1):
            p_j = primes[j]
            if p_j >= i:
                if p_j == i:
                    prev_part[j][i] = prev_part[j-1][i] + 1
                break
            i_j = 0
            for k in range(j+1):
                p_k = primes[k]
                if i-p_k < primes[k] and i-p_k >=2:
                    l = k-1
                    p_l = primes[l]
                    while i-p_k < p_l:
                        l = l-1
                        p_l = primes[l]
                    
                    i_j += prev_part[l][i-p_k]
                else:
                    i_j += prev_part[k][i-p_k]
            prev_part[j][i] = i_j
        if prev_part[len(prev_part)-1][i] >= n:
            return(i)
        i = i+1


if __name__ == '__main__':
    start = timeit.default_timer()
    res = pe_77(5000)
    end = timeit.default_timer()
    print("Result: " + str(res))
    print("Time: " + str(end-start))