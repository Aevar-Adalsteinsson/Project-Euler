import numpy as np
import timeit
import math
import itertools
import pehelperfunctions

def pe_76(n):
    prev_part = [[0],[0,1,0],[0,0,0]]#element 0,i is only referenced for i = 0
    i = 2
    while True:
        for j in range(i,1,-1):
            i_j = 0
            for k in range(1,j+1):
                i_j += prev_part[i-k][min(i-k,k)]
            prev_part[i][j] = i_j
        prev_part[i][1] = 1
        
        if i > n:
            break
        i = i+1
        
        for j in range(1,i):
            prev_part[j].append(0)
        new_list = [0]*(i+1)
        prev_part.append(new_list)
    return(prev_part[i][i]-1)

if __name__ == '__main__':
    start = timeit.default_timer()
    res = pe_76(100)
    end = timeit.default_timer()
    print("Result: " + str(res))
    print("Time: " + str(end-start))