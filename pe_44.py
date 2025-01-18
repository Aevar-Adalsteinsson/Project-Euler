import numpy as np
import timeit
import math
import itertools
import pehelperfunctions

def pe_44():
    m = 1.0
    
    while True:
        p = m*(3*m-1)/2 
        upper = int((1+np.sqrt(1+24*p))/6)+1
        for i in np.arange(1,upper):
            n = (2*p - 3*i*i + i)/(6*i)
            if n.is_integer() and n != 0:
                n_i = n+i
                
                p_n = n*(3*n-1)/2
                p_n_i = n_i*(3*n_i-1)/2
            
                p_sum = p_n_i + p_n
            
                p_sum_n = (1+np.sqrt(1+24*p_sum))/6
                if p_sum_n.is_integer():
                    return(p)
        m = m + 1

if __name__ == '__main__':
    start = timeit.default_timer()
    res = pe_44()
    end = timeit.default_timer()
    print("Result: " + str(res))
    print("Time: " + str(end-start))