import numpy as np
import timeit
import math
import itertools
import pehelperfunctions

def pe_60():
    def nested_pairs(duos,duo_primes,duo_primes_ind,duo_pairs,prime_pairs):
        n = len(prime_pairs)
        m = len(duo_primes)
        if n == 5:
            return(np.sum(prime_pairs))
        if n == 0:
            low = 0
        else:
            low = duo_primes_ind[prime_pairs[n-1]]+1
            if low >= m:
                return(None)
        for i in np.arange(low,m):
            prime = duo_primes[i]
            if all(x in duo_pairs[duo_primes_ind[prime]] for x in prime_pairs):
                prime_sum = nested_pairs(duos,duo_primes,duo_primes_ind,duo_pairs,np.append(prime_pairs,np.array([prime])))
                if prime_sum is not None:
                    return(prime_sum)
        return(None)
    def is_prime(primes,cand):
        #cand is larger than the biggest prime in primes but not larger than the square of the biggest prime
        for p in primes:
            if cand%p == 0:
                return(False)
        return(True)
    n = 10000
    primes = pehelperfunctions.gen_primes(n)
    last_prime = primes[len(primes)-1]
    
    
    duos = []
    for i in np.arange(1,len(primes)):
        p_1 = primes[i]
        p_1_dig = int(math.log10(p_1))+1
        for j in np.arange(i):
            p_2 = primes[j]
            p_2_dig = int(math.log10(p_2))+1
            
            p_12 = p_1*(10**p_2_dig) + p_2
            p_21 = p_2*(10**p_1_dig) + p_1
            
            if p_12 in primes and p_21 in primes:
                duos.append((p_1,p_2))
            if p_12 > last_prime or p_21 > last_prime:
                if int(np.sqrt(p_12)) < last_prime and int(np.sqrt(p_21)) < last_prime:
                    if is_prime(primes,p_12) and is_prime(primes,p_21):
                        duos.append((p_1,p_2))
    
    
    duo_primes = []
    for d in duos:
        p_1 = d[0]
        p_2 = d[1]
        
        if p_1 not in duo_primes:
            duo_primes.append(p_1)
        if p_2 not in duo_primes:
            duo_primes.append(p_2)
    duo_primes.sort()
    
    duo_primes_ind = {}
    for i in np.arange(len(duo_primes)):
        duo_primes_ind[duo_primes[i]] = i
    
    duo_pairs = [ [] for _ in range(len(duo_primes)) ]
    for pair in duos:
        p_1 = pair[0]
        p_2 = pair[1]
        
        duo_pairs[duo_primes_ind[p_1]].append(p_2)
        duo_pairs[duo_primes_ind[p_2]].append(p_1)
        

    prime_sum = nested_pairs(duos,duo_primes,duo_primes_ind,duo_pairs,np.array([]))
    return(int(prime_sum))

if __name__ == '__main__':
    start = timeit.default_timer()
    res = pe_60()
    end = timeit.default_timer()
    print("Result: " + str(res))
    print("Time: " + str(end-start))