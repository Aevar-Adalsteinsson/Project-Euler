import numpy as np
import timeit
import math
import itertools
import pehelperfunctions


def pe_19():
    day = 0#monday = 0, ... , sunday = 6
    year = 1900
    month = 0# Jan = 0, ... , Dec = 11
    month_inc = [31,28,31,30,31,30,31,31,30,31,30,31]
    
    day = day + sum(month_inc)#no leap year 1900
    day = day % 7
    
    mon_first = 0
    if day == 6:
        mon_first = 1
    for i in np.arange(1901,2001):
        for j in np.arange(12):
            day = day + month_inc[j]
            if j == 1 and pehelperfunctions.is_leap(i):
                day = day + 1
            day = day % 7
            if day == 6:
                mon_first = mon_first + 1
    return(mon_first)

if __name__ == '__main__':
    start = timeit.default_timer()
    res = pe_19()
    end = timeit.default_timer()
    print("Result: " + str(res))
    print("Time: " + str(end-start))