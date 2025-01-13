import numpy as np
import timeit
import math
import itertools

def pe_3(n):
    def pe_3_2(n,pf_found):
        start = pf_found + 2
        if(pf_found == 2):
            start = start - 1
        n_sq = int(np.sqrt(n)) + 1
        for i in range(start,n_sq,2):
            if(n%i == 0):
                pf_found = i
                n = n/i
                while(n%i == 0):
                    n = n/i
                if(n == 1):
                    return(pf_found)
                return(pe_3_2(n,pf_found))
        return(n)
    if(n%2 == 0):
        pf_found = 2
        n = n/2
        while(n%2 == 0):
            n = n/2
        if(n == 1):
            return(pf_found)
        return(pe_3_2(n,2))
    n_sq = int(np.sqrt(n)) + 1
    for i in range(3,n_sq,2):
        if(n%i == 0):
            pf_found = i
            n = n/i
            while(n%i == 0):
                n = n/i
            if(n == 1):
                return(pf_found)
            return(pe_3_2(n,pf_found))
    return(n)

if __name__ == '__main__':
    start = timeit.default_timer()
    res = pe_3(600851475143)
    end = timeit.default_timer()
    print("Result: " + str(res))
    print("Time: " + str(end-start))