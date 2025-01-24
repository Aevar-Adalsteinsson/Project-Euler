import numpy as np
import timeit
import math
import itertools
import pehelperfunctions

def pe_22():
    f = open("pe_22_names.txt", "r")

    names = f.read()
    names = names.split("\",\"")
    n = len(names)
    names[0] = names[0][1:]
    names[n-1] = names[n-1][:-1]
    names.sort()
    
    names_score = 0
    for i in np.arange(len(names)):
        name = names[i]
        score = 0
        for j in np.arange(len(name)):
            score += ord(name[j])-64
        names_score += (i+1)*score
    return(names_score)



if __name__ == '__main__':
    start = timeit.default_timer()
    res = pe_22()
    end = timeit.default_timer()
    print("Result: " + str(res))
    print("Time: " + str(end-start))