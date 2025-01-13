import numpy as np
import timeit
import math
import itertools
import pehelperfunctions

def pe_4():
    high = 999
    low = 100
    count = 0
    flag = True
    sum_line = high + high
    while flag:
        if sum_line%2 == 0:
            i = sum_line//2
            j = i
        else:
            i = sum_line//2
            j = i+1
        while j <= high:
            if pehelperfunctions.is_palindrome(i*j):
                flag = False
                i_found = i
                j_found = j
                high_pal = i*j
                j = high
            i = i-1
            j = j+1
        sum_line = sum_line-1
    i = i_found + 1
    j = j_found - 2
    i_pivot = i
    j_pivot = j
    while i_pivot < j_pivot:
        sum_line = i_pivot + j_pivot
        diag_line = sum_line//2
        while i < diag_line:
            if i*j > high_pal:
                if pehelperfunctions.is_palindrome(i*j):
                    high_pal = i*j
            i = i+1
            j = j-1
        i_pivot = i_pivot + 1
        j_pivot = j_pivot - 2
    return(high_pal)

if __name__ == '__main__':
    start = timeit.default_timer()
    res = pe_4()
    end = timeit.default_timer()
    print("Result: " + str(res))
    print("Time: " + str(end-start))