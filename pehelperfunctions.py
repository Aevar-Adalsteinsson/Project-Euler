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

def is_palindrome_digits(digits):
    n_digits = len(digits)
    for i in range(n_digits//2+1):
        if digits[i] != digits[n_digits-1-i]:
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

def get_prime_divisor_n(n,primes):
    #get number of prime divisors of n 
    m = len(primes)
    if n == 1:
        return(0)
    prime_div_n = 0
    for prime in primes:
        if n%prime == 0:
            prime_div_n += + 1
            while n%prime == 0:
                n = n/prime
            if n == 1:
                return(prime_div_n)
    return(prime_div_n)

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

def is_prime(primes,cand):
    n = len(primes)
    max_p = primes[n-1]
    if cand <= max_p:
        ind = np.searchsorted(primes,cand)
        if ind < n and primes[ind] == cand:
            return(True)
        else:
            return(False)
    for p in primes:
        if cand%p == 0:
            return(False)
    if cand > max_p**2:
        i = max_p + 2
        upper = int(np.sqrt(cand))+1
        while i <= upper:
            if cand%i == 0:
                return(False)
            i = i+2
    return(True)

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

def get_digits_3(n):
    n_dig = int(math.log10(n))+1
    digits = [0]*n_dig #np.zeros(n_dig)
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

def digits_sum(digs_1,digs_2):
    #digs_1 larger than digs_2
    n = len(digs_1)
    m = len(digs_2)
    carry = 0
    for i in np.arange(m):
        res = digs_1[n-1-i] + digs_2[m-1-i] + carry
        carry = res//10
        res = res%10
        digs_1[n-1-i] = res
    ind = m
    while carry != 0:
        if ind >= n:
            return(np.append(np.array([carry]),digs_1))
        res = digs_1[n-1-ind] + carry
        carry = res//10
        res = res%10
        digs_1[n-1-ind] = res
        ind = ind + 1
    return(digs_1)

def digits_prod(digs_1,digs_2):
    n = len(digs_1)
    m = len(digs_2)
    
    prod = digs_2[m-1]
    
    digs_3 = [0]*n
    carry = 0
    for i in np.arange(n):
        k = prod*digs_1[n-1-i]
        k = k+carry
        digs_3[n-1-i] = k%10
        carry = k//10
    if carry > 0:
        digs_3 = [carry] + digs_3 
    if m == 1:
        return(digs_3)
    digs = digs_1 + [0] 
    digs = digits_prod(digs, digs_2[0:(m-1)])
    return(digits_sum(digs,digs_3))

def bin_search_check(x,cand,i,j):
    if j-i == 1:
        return(x[i]==cand)
    middle = i + (j-i)//2
    comp = x[middle]
    if comp <= cand:
        return(bin_search_check(x,cand,middle,j))
    else:
        return(bin_search_check(x,cand,i,middle))

def prev_pandigital(digits,n):
    #returns the next pandigital number that is less than digits
    #n is the number of digits of digits
    #if digits is the lowest pandigital number with n digits then return digits
    index = n-1
    curr = digits[index]
    prev_digits = np.array([curr])
    count = 0
    while True:
        index = index - 1
        if index < 0:
            return(digits)
        prev = curr
        curr = digits[index]

        if curr > prev:
            break
        prev_digits = np.append(np.array([curr]),prev_digits)
    prev_digits = np.sort(prev_digits)
    next_ind = np.searchsorted(prev_digits,curr)
    prev_digits = np.flip(prev_digits)
    next_ind = len(prev_digits)-next_ind

    digits[index] = prev_digits[next_ind]
    prev_digits[next_ind] = curr
    digits = np.append(digits[:(index+1)],prev_digits)
    return(digits)

def next_pandigital(digits,n):
    #returns the next pandigital number that is higher than digits
    #n is the number of digits of digits
    #if digits is the highest pandigital number with n digits then return digits
    index = n-1
    curr = digits[index]
    prev_digits = np.array([curr])
    count = 0
    while True:
        index = index - 1
        if index < 0:
            return(digits)
        prev = curr
        curr = digits[index]

        if curr < prev:
            break
        prev_digits = np.append(np.array([curr]),prev_digits)
    prev_digits = np.sort(prev_digits)
    next_ind = np.searchsorted(prev_digits,curr, side='right')
    digits[index] = prev_digits[next_ind]
    prev_digits[next_ind] = curr
    digits = np.append(digits[:(index+1)],prev_digits)
    return(digits)

def gcd(n,m):
    if n == m:
        return(n)
    if m>n:
        temp = n
        n = m
        m = temp
    if n%m == 0:
        return(m)
    p_upp = int(np.sqrt(m))+1
    primes = gen_primes(p_upp)
    div = 1
    for p in primes:
        while m%p == 0 and n%p == 0:
            div = div*p
            m = m//p
            n = n//p
        if n <= 1 or m <= 1:
            return(div)
    return(div)
