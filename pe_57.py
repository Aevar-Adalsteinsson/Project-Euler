import numpy as np
import timeit
import math
import itertools
import pehelperfunctions

def pe_57():
    count = 0
    nom = 1
    denom = 2
    for i in np.arange(1000):
        nom = nom + 2*denom
        temp = denom
        denom = nom
        nom = temp
        nom_final = nom+denom
        if int(math.log10(nom_final)) > int(math.log10(denom)):
            count = count+1
    return(count)

if __name__ == '__main__':
    start = timeit.default_timer()
    res = pe_57()
    end = timeit.default_timer()
    print("Result: " + str(res))
    print("Time: " + str(end-start))