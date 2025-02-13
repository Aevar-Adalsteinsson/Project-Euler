import numpy as np
import timeit
import math
import itertools
import pehelperfunctions

def pe_75(L):
    def gen_pyth_prim(L):
        #generates all pythagorean primitive triples such that a+b+c <= L
        #returns list of tuples (a+b+c,a,b,c)
        #uses Euclid's formula https://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple
        n = int(np.sqrt(L)/2)+1
        prim = []
        for i in range(1,n):#i=n
            i_2 = i*i
            low = i+1
            #print((i,i_2,L))
            high = int((-i + np.sqrt(i_2+2*L))//2)+1
            for j in range(low,high,2):#j=m triples are primitive if i and j are coprime and exactly one is even
                if np.gcd(i,j) == 1:
                    j_2 = j*j
                    prim.append((2*j_2+2*j*i,j_2-i_2,2*i*j,i_2+j_2))
        return(prim)
    
    prim = gen_pyth_prim(L)

    pyth = np.zeros(L+1)
    for p in prim:
        length = p[0]
        ind = np.arange(1,L//length+1)*length
        pyth[ind] += 1
    single_tri_n = np.count_nonzero(pyth == 1)
    
    
    return(single_tri_n)

if __name__ == '__main__':
    start = timeit.default_timer()
    res = pe_75(1500000)
    end = timeit.default_timer()
    print("Result: " + str(res))
    print("Time: " + str(end-start))