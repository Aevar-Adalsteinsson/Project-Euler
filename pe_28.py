import numpy as np
import timeit
import math
import itertools
import pehelperfunctions

def pe_28(n):
    #right upper odd^2
    #left lower  even^2 + 1
    #right lower odd*even + 1
    #left upper  even*odd + 1
    
    diagonal_sum = np.sum(np.arange(1,n+1,2)**2)
    diagonal_sum = diagonal_sum + np.sum(np.arange(2,n+1,2)**2+np.ones((n-1)//2))
    main_diag = np.arange(1,n)*np.arange(2,n+1) + np.ones(n-1)
    diagonal_sum = diagonal_sum + np.sum(main_diag)
    return(diagonal_sum)

if __name__ == '__main__':
    start = timeit.default_timer()
    res = pe_28(1001)
    end = timeit.default_timer()
    print("Result: " + str(res))
    print("Time: " + str(end-start))