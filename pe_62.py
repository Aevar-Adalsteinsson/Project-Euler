import numpy as np
import timeit
import math
import itertools
import pehelperfunctions

def pe_62():
    def get_dig_occ(digits):
        #number of digit occurrences
        dig_occ = [0]*10
        n = len(digits)
        for i in np.arange(n):
            dig = digits[i]
            dig_occ[dig] = dig_occ[dig] + 1
        return(dig_occ)
    min_cube = math.inf
    for i in np.arange(3,20):
        flag = False
        digits = [0]*(i+1)
        
        low = int(10**(i/3))+1
        high = int(10**((i+1)/3))
    
    
        dig_occ = []
        for j in np.arange(low,high+1):
            digits = pehelperfunctions.get_digits_3(j)
            digits = pehelperfunctions.digits_prod(pehelperfunctions.digits_prod(digits,digits),digits)
            dig_occ.append(get_dig_occ(digits))
        dig_occ.sort()
        prev = dig_occ[0]
        cub_per_n = 1
        for j in np.arange(1,len(dig_occ)):
            curr = dig_occ[j]
            if prev == curr:
                cub_per_n = cub_per_n + 1
            else:
                cub_per_n = 1
            prev = curr
            if cub_per_n > 3:
                if cub_per_n == 5:
                    flag = True
                    for k in np.arange(low,high+1):
                        digits = pehelperfunctions.get_digits_3(k)
                        digits = pehelperfunctions.digits_prod(pehelperfunctions.digits_prod(digits,digits),digits)
                        occ = get_dig_occ(digits)
                        if occ == curr:
                            if k < min_cube:
                                min_cube = k
        if flag:
            break
    return(int(min_cube)**3)

if __name__ == '__main__':
    start = timeit.default_timer()
    res = pe_62()
    end = timeit.default_timer()
    print("Result: " + str(res))
    print("Time: " + str(end-start))