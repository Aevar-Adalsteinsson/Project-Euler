import numpy as np
import timeit
import math
import itertools
import matplotlib.pyplot as plt

def is_palindrome(n):
    #checks if an integer n is a palindrome
    n_str = str(n)
    n_str_rev = n_str[::-1]
    return(n_str == n_str_rev)

def gen_primes(n):
    prime_cand = np.arange(2,n+1)
    upper_bound = n/np.log(n)*1.25506
    upper_bound = int(np.ceil(upper_bound)) + 1
    index_p = 0
    index_primes = 0
    primes = np.zeros(upper_bound,dtype = int)
    m = len(prime_cand)
    while index_p < m:
        prime = prime_cand[index_p]
        if prime > 0:
            primes[index_primes] = prime
            index_primes = index_primes + 1
            index = np.arange(2,n//prime+1)*prime-2
            prime_cand[index] = 0
        index_p = index_p + 1
    return(primes[0:index_primes])