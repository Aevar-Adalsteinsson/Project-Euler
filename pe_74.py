import numpy as np
import timeit
import math
import itertools
import pehelperfunctions

def pe_74(n):
    def get_digit_factorial(n):
        fact_sum = 0
        while n > 0:
            fact_sum += math.factorial(n%10)
            n = n//10
        return(fact_sum)
    term_60 = 0
    found = [1]*n
    digit_fact = {1:1,2:2,145:1,169:3,363601:3,1454:3,871:2,45361:2,872:2,45361:2,40585:1}

    for i in range(3,n):
        if found[i] == 0:
            continue
        chain = [i]
        curr = i
        while curr not in digit_fact:
            fact_sum = get_digit_factorial(curr)
            chain.append(fact_sum)
            curr = fact_sum
        inc = digit_fact[curr]
        m = len(chain)
        for j in range(m):
            chain_j = chain[j]
            val = m-1-j+inc
            if chain_j < n:
                found[chain_j] = 0
            if chain_j < n and val == 60:
                term_60 += 1
            digit_fact[chain_j] = val
    return(term_60)

if __name__ == '__main__':
    start = timeit.default_timer()
    res = pe_74(10**6)
    end = timeit.default_timer()
    print("Result: " + str(res))
    print("Time: " + str(end-start))