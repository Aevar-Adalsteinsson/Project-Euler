import numpy as np
import timeit
import math
import itertools
import pehelperfunctions


PE_8_STRING = arg = """73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450"""





def pe_1(p1,p2,n):
#https://projecteuler.net/problem=1
    if(p1%p2 == 0):
        return(sum(range(p2,n,p2)))
    if(p2%p1 == 0):
        return(sum(range(p1,n,p1)))
    factor_sum = sum(range(p1,n,p1)) + sum(range(p2,n,p2)) - sum(range(p1*p2,n,p1*p2)) 
    return(factor_sum)

def pe_2(n):
#https://projecteuler.net/problem=2
    fib_even = 0
    fib = 2   # fib n
    fib_p = 1 # fib n-1
    while fib<n:
        fib_even = fib_even + fib
        fib_temp = fib + fib_p #odd fib n+1
        fib_p = fib + fib_temp #odd fib n+2
        fib = fib_temp + fib_p #even fib n+3 => fib n
    return(fib_even)

def pe_3(n):
#https://projecteuler.net/problem=3
    def pe_3_2(n,pf_found):
        start = pf_found + 2
        if(pf_found == 2):
            start = start - 1
        n_sq = int(np.sqrt(n)) + 1
        for i in range(start,n_sq,2):
            if(n%i == 0):
                pf_found = i
                n = n/i
                while(n%i == 0):
                    n = n/i
                if(n == 1):
                    return(pf_found)
                return(pe_3_2(n,pf_found))
        return(n)
    if(n%2 == 0):
        pf_found = 2
        n = n/2
        while(n%2 == 0):
            n = n/2
        if(n == 1):
            return(pf_found)
        return(pe_3_2(n,2))
    n_sq = int(np.sqrt(n)) + 1
    for i in range(3,n_sq,2):
        if(n%i == 0):
            pf_found = i
            n = n/i
            while(n%i == 0):
                n = n/i
            if(n == 1):
                return(pf_found)
            return(pe_3_2(n,pf_found))
    return(n)

def pe_4():
    high = 999
    low = 100
    count = 0
    flag = True
    sum_line = high + high
    while flag:
        if sum_line%2 == 0:
            i = sum_line//2
            j = i
        else:
            i = sum_line//2
            j = i+1
        while j <= high:
            if pehelperfunctions.is_palindrome(i*j):
                flag = False
                i_found = i
                j_found = j
                high_pal = i*j
                j = high
            i = i-1
            j = j+1
        sum_line = sum_line-1
    i = i_found + 1
    j = j_found - 2
    i_pivot = i
    j_pivot = j
    while i_pivot < j_pivot:
        sum_line = i_pivot + j_pivot
        diag_line = sum_line//2
        while i < diag_line:
            if i*j > high_pal:
                if pehelperfunctions.is_palindrome(i*j):
                    high_pal = i*j
            i = i+1
            j = j-1
        i_pivot = i_pivot + 1
        j_pivot = j_pivot - 2
    return(high_pal)

def pe_5(n):
    primes = pehelperfunctions.gen_primes(n)
    f_x = lambda x: int(np.log(n)/np.log(x))
    mapf = np.vectorize(f_x)
    prime_mult = mapf(primes)
    factors = primes ** prime_mult
    return(np.prod(factors))

def pe_6(n):
    nums = np.arange(1,n+1)
    nums_sum = n*(n+1)/2
    nums_sq = nums ** 2
    return(nums_sum**2 - np.sum(nums_sq))

def pe_7(n):
    upper = n*(np.log(n) + np.log(np.log(n)))
    primes = pehelperfunctions.gen_primes(int(upper))
    return(primes[n-1])

def pe_8(n_str):
    n_char = [*n_str]
    n_char = [x for x in n_char if x != '\n']
    digits = np.array(n_char,dtype = float)
    n = len(digits)
    
    def non_zero_prod(start,end,n,digits):
        if end >= n:
            return((0,start,end))
        i = start
        prod_13 = 1.0
        while i <= end:
            if digits[i] == 0:
                i = i+1
                start = i
                end = start + 12
                if end >= n:
                    return((0,start,end))
                prod_13 = 1.0
            else:
                prod_13 = prod_13*digits[i]
                i = i+1
        return((prod_13,start,end))
    prod_13,start,end = non_zero_prod(0,12,n,digits)
    if end >= n:
        return(prod_13)
    max_prod = prod_13
    start = start + 1
    end = end + 1
    while end<n:
        digit_end = digits[end]
        digit_start = digits[start-1]
        if digit_end == 0:
            prod_13,start,end = non_zero_prod(end+1,end+13,n,digits)
            max_prod = np.maximum(max_prod,prod_13)
            if prod_13 == 0:
                return(max_prod)
            if end >= n:
                return(max_prod)
            start = start + 1
            end = end + 1
        else:
            prod_13 = (prod_13*digit_end)/digit_start
            max_prod = np.maximum(max_prod,prod_13)
            start = start + 1
            end = end + 1
    return(max_prod)

def pe_9(n):
    a_upper = n//3 - 1
    for a in range(1,a_upper+1):
        if (n-a)%2 == 0:
            b_upper = (n-a)/2 - 1
        else:
            b_upper = (n-a)//2
        b_upper = (n-a)
        b = np.arange(a+1,b_upper+1)
        c = n - b - a
        pyth_ab = a**2 + b**2
        pyth_c = c**2
        index = np.where((pyth_ab - pyth_c) == 0)
        if index[0].size == 1:
            b = b[index[0]][0]
            c = c[index[0]][0]
            return(a*b*c)

def pe_10(n):
    primes = pehelperfunctions.gen_primes(n)
    return(np.sum(primes,dtype = np.int64))





if __name__ == '__main__':
    completed = [1,2,3,4,5,6,7,8,9,10]
    inputs = {1:(3,5,1000),2:(4000000,),3:(600851475143,),4:(),5:(20,),6:(100,),7:(10001,),8:(PE_8_STRING,),9:(1000,),10:(2000000,)}
    for i in completed:
        pe_func = "pe_" + str(i)
        args = inputs[i]
        exec(f"x = {pe_func}")

        start = timeit.default_timer()
        res = x(*args)
        end = timeit.default_timer()
        print("Problem: " + str(i))
        print("Result: " + str(res))
        print("Time: " + str(end-start))