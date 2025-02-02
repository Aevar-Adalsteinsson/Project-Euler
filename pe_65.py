import numpy as np
import timeit
import math
import itertools
import pehelperfunctions

def pe_65(n):
    def rat_approx(plus_term,periods):
        n = len(periods)
        nom = 1
        denom = periods[n-1]
        inter = (nom,denom)
        for i in range(n-2,-1,-1):
            denom = inter[1]
            nom = periods[i]*denom + inter[0]
    
            temp = denom
            denom = nom
            nom = temp
    
            inter = (nom,denom)
        nom = nom + plus_term*denom
        return((nom,denom))
    
    plus_term = 2
    periods = [0]*(n-1)
    for i in range(n-1):
        if i%3 == 1:
            periods[i] = (i//3+1)*2
        else:
            periods[i] = 1
    nom,denom = rat_approx(plus_term,periods)
    digit_sum = 0
    while nom > 0:
        digit_sum += nom%10
        nom = nom//10
    return(digit_sum)

if __name__ == '__main__':
    start = timeit.default_timer()
    res = pe_65(100)
    end = timeit.default_timer()
    print("Result: " + str(res))
    print("Time: " + str(end-start))