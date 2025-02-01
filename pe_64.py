import numpy as np
import timeit
import math
import itertools
import pehelperfunctions

def pe_64():
    odd_p = 0
    for i in np.arange(2,10001):
        count = 0
        a = i
        b = int(np.sqrt(a))
        c = np.sqrt(a)
        if b == c:
            continue
        
        per = []
        nom = [0,1]
        denom = [1,-b]
        
        initial = []
        while True:
            init = (nom[1],denom[0],denom[1])
            if init in initial:
                if len(per)%2 == 1:
                    odd_p = odd_p + 1
                break
            else:
                initial = initial + [init]
            count = count + 1
            


            temp = nom.copy()
            nom[0] = denom[0]*temp[1]
            nom[1] = (-denom[1])*temp[1]

            denom[0] = 0
            denom[1] = a-denom[1]*denom[1]

            div = pehelperfunctions.gcd(np.abs(nom[0]),np.abs(nom[1]))
            div = pehelperfunctions.gcd(div,np.abs(nom[1]))

            nom = [x/div for x in nom]
            denom = [x/div for x in denom]

            whole = (nom[0]*c + nom[1])//denom[1]
            nom[1] = nom[1] - whole*denom[1]
            
            
            
            temp = nom
            nom = denom
            denom = temp
            
            per = per + [whole]
    print(odd_p)

if __name__ == '__main__':
    start = timeit.default_timer()
    res = pe_64()
    end = timeit.default_timer()
    print("Result: " + str(res))
    print("Time: " + str(end-start))