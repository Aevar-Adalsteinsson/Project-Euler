import numpy as np
import timeit
import math
import itertools
import pehelperfunctions

def pe_51():
    n = 1000000
    primes = pehelperfunctions.gen_primes(n)
    
    
    max_rep = 0
    for p in primes[4:]:
        digits_n = int(math.log10(p))+1
        
        dig_012 = np.zeros(3,dtype = int)
        dig_012_place = [[],[],[]]
        p_dig = p #replacing the last digit can only produce at most 4 prime digit replacements
        dig_ind = 0
        while p_dig != 0:
            dig = p_dig%10
            if dig < 3:
                dig_012[dig] = dig_012[dig] + 1
                dig_012_place[dig].append(dig_ind)
            p_dig = p_dig//10
            dig_ind = dig_ind + 1
        last_dig = p%10
        if last_dig < 3:
            dig_012[last_dig] = dig_012[last_dig] - 1
        

        for i in np.arange(len(dig_012)):
            dig_i = dig_012[i]
            if dig_i == 0:
                continue
            
            if last_dig == i:
                place_inc = 1
            else:
                place_inc = 0
            for j in np.arange(1,2**dig_i):
                indices = list(format(j,'#0' + str(dig_i+2) + 'b')[2:])
                indices = list(map(int, indices))
                
                
                increment = 0
                for k in np.arange(len(indices)):
                    index = indices[k]
                    if index == 1:
                        increment = increment + 10**dig_012_place[i][k + place_inc]
                    
                

                p_cand = p - i*increment
                
                p_cand_ind = 0
                if digits_n-1 in dig_012_place[i]:#candidates must have the same number of digits

                    p_cand = p_cand + increment
                    p_cand_ind = p_cand_ind + 1
                
                p_count = 0
                while p_cand_ind < 10:
                    if p_cand in primes:
                        p_count = p_count + 1
                    p_cand = p_cand + increment
                    p_cand_ind = p_cand_ind + 1
                if p_count > max_rep:
                    max_rep = p_count
                    if p_count == 8:
                        return(p)

if __name__ == '__main__':
    start = timeit.default_timer()
    res = pe_51()
    end = timeit.default_timer()
    print("Result: " + str(res))
    print("Time: " + str(end-start))