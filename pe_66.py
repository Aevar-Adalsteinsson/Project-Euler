import numpy as np
import timeit
import math
import itertools
import pehelperfunctions

def pe_66(n):
    def per_sqrt(nom,denom,n,root_n):
        temp = nom.copy()
        nom[0] = denom[0]*temp[1]
        nom[1] = (-denom[1])*temp[1]

        denom[0] = 0
        denom[1] = n-denom[1]*denom[1]

        div = pehelperfunctions.gcd(np.abs(nom[0]),np.abs(nom[1]))
        div = pehelperfunctions.gcd(div,np.abs(nom[1]))

        nom = [x/div for x in nom]
        denom = [x/div for x in denom]

        whole = int((nom[0]*root_n + nom[1])//denom[1])
        nom[1] = nom[1] - whole*denom[1]

        temp = nom
        nom = denom
        denom = temp
        return((nom,denom,whole))
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
    
    max_dio = 0
    for D in range(8,n+1):
        D_sqrt = int(np.sqrt(D))
        if D_sqrt**2 == D:
            continue
        nom = [0,1]
        denom = [1,-D_sqrt]
        periods = []
        while True:
            nom,denom,whole = per_sqrt(nom,denom,D,np.sqrt(D))#numerator and denom for producing periodic continuing fractions
            periods.append(whole)
            nom_2 ,denom_2 = rat_approx(D_sqrt,periods)#rational approximation of square root of D using continuing fractions
            
            x_2 = nom_2*nom_2
            Dy_2 = D*denom_2*denom_2
            if x_2-Dy_2 == 1:
                if nom_2 > max_dio:
                    max_dio = nom_2
                break
    return(max_dio)

if __name__ == '__main__':
    start = timeit.default_timer()
    res = pe_66(1000)
    end = timeit.default_timer()
    print("Result: " + str(res))
    print("Time: " + str(end-start))