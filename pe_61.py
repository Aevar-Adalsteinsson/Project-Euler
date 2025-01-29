import numpy as np
import timeit
import math
import itertools
import pehelperfunctions

def pe_61():
    def cyclic_6(cycle,cycle_dict,num_rem,last_2):
        m = len(num_rem)
        if m == 0:
            n_1 = cycle[0]
            n_2 = cycle[len(cycle)-1]
            if n_1//100 == n_2%100:
                return(np.sum(cycle))
            return(None)
    
        for i in np.arange(m):
            num_type = num_rem[i]
            k = last_2*100
            n_cand = num_type-1 + np.sqrt(num_type**2 -2*num_type + 1 + 8*k + 8*num_type*k)
            n_cand = n_cand/(2 + 2*num_type)
            n_cand = int(n_cand)
        
            n_2 = int((n_cand+1)*((n_cand+2)/2+num_type*n_cand/2))
        
            if n_2//100 == last_2 and (n_2%100)//10 != 0:
                cycle_dict[num_type] = n_2
                cycle_2 = np.append(cycle,np.array([n_2],dtype = int))
                num_rem_2 = np.delete(num_rem,i)
            
                val = cyclic_6(cycle_2,cycle_dict,num_rem_2,n_2%100)
                if val is not None:
                    return(val)
        return(None)
    
    
    for i in np.arange(18,58):
        cycle = np.zeros(1,dtype = int)
        cycle_dict = {}
        cycle_ind = 0
        num_type = 5
        
        n = int(i*((i+1)/2+num_type*(i-1)/2))
        last_2 = n%100
        if last_2//10 == 0:
            continue
        cycle[cycle_ind] = n
        cycle_dict[cycle_ind] = num_type
        cycle_ind = cycle_ind + 1
        val = cyclic_6(cycle,cycle_dict,np.arange(5),last_2)
        if val is not None:
            return(val)

if __name__ == '__main__':
    start = timeit.default_timer()
    res = pe_61()
    end = timeit.default_timer()
    print("Result: " + str(res))
    print("Time: " + str(end-start))