import numpy as np
import timeit
import math
import itertools
import pehelperfunctions

def pe_34():
    fact = [math.factorial(x) for x in range(10)]
    max_8 = fact[8]*6 #8!*6 has 6 digits and 8!*7 has 6 digits
    fact_digit_sum = 0
    i = 10
    while i < 2540160:# for i in range(10,2540160):
        digits = []
        max_digit = 0
        i_1 = i
        n_9 = 0
        while i_1 > 0:
            digit = i_1%10
            if digit > max_digit:
                max_digit = digit
            if digit == 9:
                n_9 += 1
            digits.append(digit)
            i_1 = i_1//10
        if max_digit == 9:
            if i < fact[9]:
                i = i+1
                continue
            if i > n_9*fact[9] + (7-n_9)*fact[8]:#i needs to have more digits that are 9
                pow_10 = 1
                while i%(10**pow_10) == 9:
                    pow_10 += 1
                i = i - i%(10**pow_10) + 10**pow_10 - 1
        else:
            if i > max_8:
                i = i - i%10+9#
                continue
        fact_sum = 0
        for j in digits:
            fact_sum += fact[j]
        if fact_sum == i:
            fact_digit_sum += i
        i = i+1
    return(fact_digit_sum)

if __name__ == '__main__':
    start = timeit.default_timer()
    res = pe_34()
    end = timeit.default_timer()
    print("Result: " + str(res))
    print("Time: " + str(end-start))