import numpy as np
import timeit
import math
import itertools
import pehelperfunctions

def pe_55():
    def reverse_num(digits):
        n = len(digits)
        rev = np.zeros(n)
        for i in np.arange(n):
            rev[i] = digits[n-1-i]
        return(rev)
    lych_n = 0
    for i in np.arange(5,10000):
        count = 0
        lychrel_cand = pehelperfunctions.get_digits_2(i)
        flag = True
        while count <= 50:
            rev = reverse_num(lychrel_cand)
            lychrel_cand = pehelperfunctions.digits_sum(lychrel_cand,rev)
            if pehelperfunctions.is_palindrome_digits(lychrel_cand):
                flag = False
                break
            count = count + 1
        if flag:
            lych_n = lych_n + 1
    return(lych_n)

if __name__ == '__main__':
    start = timeit.default_timer()
    res = pe_55()
    end = timeit.default_timer()
    print("Result: " + str(res))
    print("Time: " + str(end-start))