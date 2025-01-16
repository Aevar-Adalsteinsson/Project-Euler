import numpy as np
import timeit
import math
import itertools
import pehelperfunctions

def pe_32():
    digits = np.zeros(9,dtype = int)
    pan_prods = np.empty(0,dtype = int)
    for i in range(2,99):
        i_dig = int(math.log10(i)) + 1
        if i_dig == 1:
            digits[0] = i
        else:
            digits[0] = i%10
            quotient = i//10
            if quotient == 0 or quotient == digits[0]:
                continue
            digits[1] = quotient
        #lower bound for j = 10**(4-i_dig)
        #upper bound for j = 10**5/i
        for j in range(10**(4-i_dig),10000//i+1):
            digits[i_dig:] = np.zeros(9-i_dig,dtype = int)
            
            j2 = j
            digit_index = i_dig-1
            flag = False
            while j2>0:
                digit_index = digit_index + 1
                rem = j2%10
                j2 = j2//10
                if rem == 0 or rem in digits[:digit_index]:#pandigital condition
                    flag = True
                    break
                digits[digit_index] = rem
            if flag:
                continue
            product = i*j
            
            prod_dig = int(math.log10(product)) + 1
            if prod_dig+1+4 != 9:
                continue
            
            product2 = product
            while product2>0:
                digit_index = digit_index + 1
                rem = product2%10
                product2 = product2//10
                if rem == 0 or rem in digits[:digit_index]:#pandigital condition
                    flag = True
                    break
                digits[digit_index] = rem
            if flag:
                continue
            if product not in pan_prods:
                pan_prods = np.append(pan_prods,np.array([product]))
    return(np.sum(pan_prods))

if __name__ == '__main__':
    start = timeit.default_timer()
    res = pe_32()
    end = timeit.default_timer()
    print("Result: " + str(res))
    print("Time: " + str(end-start))