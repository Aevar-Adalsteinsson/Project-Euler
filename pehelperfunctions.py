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

def is_palindrome_str(s):
    #more primite solution might be quicker
    n = len(s)
    if n <= 1:
        return(True)
    for i in np.arange(n//2):
        if not s[i] == s[n-1-i]:
            return(False)
    return(True)

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

def get_prime_divisors(n,primes,primes_ind):
    #get prime divisors of n 
    #returns list of prime divisor multiplicity of primes up to n 
    #e.g n = 2^k*3^r gives [k,3,0,...,0]
    m = len(primes)
    if n == 1:
        return(np.zeros(m))
    divisors = np.zeros(m)
    for prime in primes:
        while n%prime == 0:
            n = n/prime
            index = primes_ind[prime]
            divisors[index] = divisors[index] + 1
    return(divisors)

def gen_additional_primes(n,primes,primes_ind):
    #primes must contain 2 and 3
    #primes contains all primes less than some k < n
    #generates all primes up to n
    prime_cand = np.arange(2,n+1)
    for prime in primes:
        index = np.arange(2,n//prime+1)*prime-2
        prime_cand[index] = 0
    index_p = primes[len(primes)-1]
    primes_ind_n = len(primes_ind)
    
    m = len(prime_cand)
    while index_p < m:
        prime = prime_cand[index_p]
        if prime > 0:
            primes_ind[prime] = primes_ind_n
            primes_ind_n = primes_ind_n + 1
            index = np.arange(2,n//prime+1)*prime-2
            prime_cand[index] = 0
        index_p = index_p + 2
    primes = prime_cand[np.nonzero(prime_cand)[0]]
    return(primes, primes_ind)

def gen_additional_primes_2(n,primes):
    #primes verdur ad innihalda ad minnsta kosti 2 og 3
    #generates all primes up to n using primes up to some value k < n%prime
    #same as gen_additional_primes but does not use primes_ind
    prime_cand = np.arange(2,n+1)
    for prime in primes:
        index = np.arange(2,n//prime+1)*prime-2
        prime_cand[index] = 0
    index_p = primes[len(primes)-1]
    
    m = len(prime_cand)
    while index_p < m:
        prime = prime_cand[index_p]
        if prime > 0:
            index = np.arange(2,n//prime+1)*prime-2
            prime_cand[index] = 0
        index_p = index_p + 2
    primes = prime_cand[np.nonzero(prime_cand)[0]]
    return(primes)

def is_leap(year):
    #works for positive years
    y_4 = year % 4
    if y_4 != 0:
        return(False)
    y_100 = year % 100
    y_400 = year % 400
    if y_100 == 0 and y_400 != 0:
        return(False)
    return(True)

def divisor_sum(divisors,prime_key,n):
    #returns the sum of proper divisors of n
    m = len(divisors)
    div_iter = [range(i+1) for i in divisors]
    if m > 1:
        set_mult = itertools.product(div_iter[0],div_iter[1])
        for i in range(2,m):
            set_mult = itertools.product(set_mult,div_iter[i])

    else:
        set_mult = [(i) for i in range(divisors[0]+1)]
    div_sum = 0
    for i in set_mult:
        prod = 1
        prime_index = len(divisors)-1
        while not isinstance(i,int) :
            prod = prod * (prime_key[prime_index]**i[1])
            prime_index = prime_index-1
            i = i[0]
        prod = prod * (prime_key[0]**i)
        div_sum = div_sum + prod
    return(div_sum-n)

def get_digits(digits,n):
    rem = n%10
    n = n//10
    digit_index = 0
    while n > 0:
        digits[digit_index] = rem
        digit_index = digit_index + 1
        rem = n%10
        n = n//10
    digits[digit_index] = rem
    return(digits,digit_index+1)

def get_digits_2(n):
    n_dig = int(math.log10(n))+1
    digits = np.zeros(n_dig)
    rem = n%10
    n = n//10
    digit_index = n_dig-1
    while n > 0:
        digits[digit_index] = rem
        digit_index = digit_index - 1
        rem = n%10
        n = n//10
    digits[digit_index] = rem
    return(digits)

def bin_search_check(x,cand,i,j):
    if j-i == 1:
        return(x[i]==cand)
    middle = i + (j-i)//2
    comp = x[middle]
    if comp <= cand:
        return(bin_search_check(x,cand,middle,j))
    else:
        return(bin_search_check(x,cand,i,middle))






