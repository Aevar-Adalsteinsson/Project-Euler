import numpy as np
import timeit
import math
import itertools
import pehelperfunctions


def pe_17():
    n_digits_letters = [3,3,5,4,4,3,5,5,4]#one,two,...,nine
    n_digits_sum = sum(n_digits_letters)
    
    n_teen_letters = [6,6,8,8,7,7,9,8,8]#eleven,twelve,...,nineteen
    n_teen_sum = sum(n_teen_letters)
    
    n_ten = 3
    n_tens_letters = [6,6,5,5,5,7,6,6]#twenty, ... ,ninety
    n_tens_sum = sum(n_tens_letters)
    
    n_hundred = 7 #hundred
    n_thousand = 8 #thousand
    n_and = 3
    
    n_2digits = n_digits_sum + n_ten + n_teen_sum + 10*n_tens_sum + 8*n_digits_sum
    n_3digits = n_2digits + (n_digits_sum + 9*n_hundred) + (9*n_2digits + 99*(n_digits_sum + 9*n_hundred + 9*n_and)) + 3 + n_thousand

    return(n_3digits)

if __name__ == '__main__':
    start = timeit.default_timer()
    res = pe_17()
    end = timeit.default_timer()
    print("Result: " + str(res))
    print("Time: " + str(end-start))