import numpy as np
import timeit
import math
import itertools
import pehelperfunctions

def pe_8(n_str):
    n_char = [*n_str]
    n_char = [x for x in n_char if x != '\n']
    digits = np.array(n_char,dtype = float)
    n = len(digits)
    
    def non_zero_prod(start,end,n,digits):
        if end >= n:
            return((0,start,end))
        i = start
        prod_13 = 1.0
        while i <= end:
            if digits[i] == 0:
                i = i+1
                start = i
                end = start + 12
                if end >= n:
                    return((0,start,end))
                prod_13 = 1.0
            else:
                prod_13 = prod_13*digits[i]
                i = i+1
        return((prod_13,start,end))
    prod_13,start,end = non_zero_prod(0,12,n,digits)
    if end >= n:
        return(prod_13)
    max_prod = prod_13
    start = start + 1
    end = end + 1
    while end<n:
        digit_end = digits[end]
        digit_start = digits[start-1]
        if digit_end == 0:
            prod_13,start,end = non_zero_prod(end+1,end+13,n,digits)
            max_prod = np.maximum(max_prod,prod_13)
            if prod_13 == 0:
                return(max_prod)
            if end >= n:
                return(max_prod)
            start = start + 1
            end = end + 1
        else:
            prod_13 = (prod_13*digit_end)/digit_start
            max_prod = np.maximum(max_prod,prod_13)
            start = start + 1
            end = end + 1
    return(max_prod)

if __name__ == '__main__':
    arg = """73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450"""
    start = timeit.default_timer()
    res = pe_8(arg)
    end = timeit.default_timer()
    print("Result: " + str(res))
    print("Time: " + str(end-start))