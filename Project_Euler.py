import numpy as np
import timeit
import math
import itertools
import pehelperfunctions


PE_8_STRING = """73167176531330624919225119674426574742355349194934
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
PE_11_STRING = """08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"""
PE_13_STRING = """37107287533902102798797998220837590246510135740250
46376937677490009712648124896970078050417018260538
74324986199524741059474233309513058123726617309629
91942213363574161572522430563301811072406154908250
23067588207539346171171980310421047513778063246676
89261670696623633820136378418383684178734361726757
28112879812849979408065481931592621691275889832738
44274228917432520321923589422876796487670272189318
47451445736001306439091167216856844588711603153276
70386486105843025439939619828917593665686757934951
62176457141856560629502157223196586755079324193331
64906352462741904929101432445813822663347944758178
92575867718337217661963751590579239728245598838407
58203565325359399008402633568948830189458628227828
80181199384826282014278194139940567587151170094390
35398664372827112653829987240784473053190104293586
86515506006295864861532075273371959191420517255829
71693888707715466499115593487603532921714970056938
54370070576826684624621495650076471787294438377604
53282654108756828443191190634694037855217779295145
36123272525000296071075082563815656710885258350721
45876576172410976447339110607218265236877223636045
17423706905851860660448207621209813287860733969412
81142660418086830619328460811191061556940512689692
51934325451728388641918047049293215058642563049483
62467221648435076201727918039944693004732956340691
15732444386908125794514089057706229429197107928209
55037687525678773091862540744969844508330393682126
18336384825330154686196124348767681297534375946515
80386287592878490201521685554828717201219257766954
78182833757993103614740356856449095527097864797581
16726320100436897842553539920931837441497806860984
48403098129077791799088218795327364475675590848030
87086987551392711854517078544161852424320693150332
59959406895756536782107074926966537676326235447210
69793950679652694742597709739166693763042633987085
41052684708299085211399427365734116182760315001271
65378607361501080857009149939512557028198746004375
35829035317434717326932123578154982629742552737307
94953759765105305946966067683156574377167401875275
88902802571733229619176668713819931811048770190271
25267680276078003013678680992525463401061632866526
36270218540497705585629946580636237993140746255962
24074486908231174977792365466257246923322810917141
91430288197103288597806669760892938638285025333403
34413065578016127815921815005561868836468420090470
23053081172816430487623791969842487255036638784583
11487696932154902810424020138335124462181441773470
63783299490636259666498587618221225225512486764533
67720186971698544312419572409913959008952310058822
95548255300263520781532296796249481641953868218774
76085327132285723110424803456124867697064507995236
37774242535411291684276865538926205024910326572967
23701913275725675285653248258265463092207058596522
29798860272258331913126375147341994889534765745501
18495701454879288984856827726077713721403798879715
38298203783031473527721580348144513491373226651381
34829543829199918180278916522431027392251122869539
40957953066405232632538044100059654939159879593635
29746152185502371307642255121183693803580388584903
41698116222072977186158236678424689157993532961922
62467957194401269043877107275048102390895523597457
23189706772547915061505504953922979530901129967519
86188088225875314529584099251203829009407770775672
11306739708304724483816533873502340845647058077308
82959174767140363198008187129011875491310547126581
97623331044818386269515456334926366572897563400500
42846280183517070527831839425882145521227251250327
55121603546981200581762165212827652751691296897789
32238195734329339946437501907836945765883352399886
75506164965184775180738168837861091527357929701337
62177842752192623401942399639168044983993173312731
32924185707147349566916674687634660915035914677504
99518671430235219628894890102423325116913619626622
73267460800591547471830798392868535206946944540724
76841822524674417161514036427982273348055556214818
97142617910342598647204516893989422179826088076852
87783646182799346313767754307809363333018982642090
10848802521674670883215120185883543223812876952786
71329612474782464538636993009049310363619763878039
62184073572399794223406235393808339651327408011116
66627891981488087797941876876144230030984490851411
60661826293682836764744779239180335110989069790714
85786944089552990653640447425576083659976645795096
66024396409905389607120198219976047599490197230297
64913982680032973156037120041377903785566085089252
16730939319872750275468906903707539413042652315011
94809377245048795150954100921645863754710598436791
78639167021187492431995700641917969777599028300699
15368713711936614952811305876380278410754449733078
40789923115535562561142322423255033685442488917353
44889911501440648020369068063960672322193204149535
41503128880339536053299340368006977710650566631954
81234880673210146739058568557934581403627822703280
82616570773948327592232845941706525094512325230608
22918802058777319719839450180888072429661980811197
77158542502016545090413245809786882778948721859617
72107838435069186155435662884062257473692284509516
20849603980134001723930671666823555245252804609722
53503534226472524250874054075591789781264330331690"""
PE_18_STRING = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''


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

def pe_11(grid):
    def prepare_arg_11(grid):
        grid = grid.split('\n')
        grid = np.array(grid)
        n = len(grid)
        m = len(grid[0].split(' '))
        grid_2 = np.zeros((n,m))
        for i in range(n):
            grid_2[i,0:m] = np.array(grid[i].split(' '), dtype = int)
        return(grid_2)
    grid = prepare_arg_11(grid)
    n = len(grid)
    m = len(grid[0])
    max_prod = 0
    for i in range(n):
        for j in range(n-3):
            prod_lat = np.prod(grid[i,j:(j+4)])
            prod_hor = np.prod(grid[j:(j+4),i])
            max_prod = np.max(np.array([max_prod,prod_lat,prod_hor]))
    for s in range(4,n + m -4):
        if s > (n-1):
            i = s%19
            j = 19
        else:
            i = 0
            j = s
        while i + 4 <= n and j-4 >= 0:
            ind_1 = np.arange(i,i+4)
            ind_2 = np.arange(j,j-4,-1)
            prod_off = np.prod(grid[ind_1,ind_2])
            prod_main = np.prod(grid[n-1-ind_1,ind_2])
            max_prod = np.max(np.array([max_prod,prod_main,prod_off]))
            i = i + 1
            j = j - 1
    return(max_prod)

def pe_12(n):
    m = 2
    primes = np.array([2,3])
    primes_ind = {2:0,3:1}
    primes_up_to = 3
    prev_divisors = np.array([0,1])
    while True:
        tri = m*(m+1)/2
        if m+1 > primes_up_to:
            old_len = len(primes)
            primes, primes_ind = pehelperfunctions.gen_additional_primes(10*primes_up_to,primes,primes_ind)
            primes_up_to = 10*primes_up_to
            new_len = len(primes)
            prev_divisors = np.append(prev_divisors,np.zeros(new_len-old_len))
        if m%2 == 0:
            divisors_2 = pehelperfunctions.get_prime_divisors(m+1,primes,primes_ind)
        else:
            divisors_2 = pehelperfunctions.get_prime_divisors((m+1)/2,primes,primes_ind)
        divisors_1 = prev_divisors
        prev_divisors = divisors_2
        divisors = divisors_1 + divisors_2
        factors = np.prod(divisors+1)
        if factors > n:
                return(tri)
        m = m+1

def pe_13(n_str):
    n_str = n_str.split('\n')
    n = len(n_str)
    m = len(n_str[0])
    grid = np.empty((n,m),dtype = int)
    for i in range(n):
        grid[i,:] = [*n_str[i]]
    first_sum = np.sum(grid[:,0])
    
    extra_digits = int(math.log10(first_sum))# extra_digits er einum minna en digits i first sum
    n_digits = extra_digits + m
    digits = np.zeros(n_digits,dtype = int)
    
    first_sum = [*str(first_sum)]
    first_sum = np.array(first_sum,dtype = int)
    digits[:(extra_digits+1)] = digits[:(extra_digits+1)] + first_sum
    for i in range(1,m):
        sum_i = np.sum(grid[:,i])
        sum_i = np.array([*str(sum_i)],dtype = int)
        n_i = len(sum_i)
        digits[(extra_digits+i+1-n_i):(extra_digits+i+1)] = digits[(extra_digits+i+1-n_i):(extra_digits+i+1)] + sum_i
    carry = 0
    for i in range(n_digits-1,-1,-1):
        total = carry+digits[i]
        carry = total//10
        digit = total%10
        digits[i] = digit
    if carry > 0:
        digits = np.append(carry,digits)
    s = ""
    for digit in digits:
        s = s + str(digit)
    return(s)

def pe_14(n):
    dist_dict = {1:1}
    max_dist = 1
    max_n = 1
    index = 2
    while index <= n:
        curr = index
        chain = np.empty(0)
        while curr not in dist_dict:
            chain = np.append(chain,curr)
            if curr%2 == 0:
                curr = curr//2
            else:
                curr = curr*3+1
        chain_n = len(chain)
        chain_rem_n = dist_dict[curr]
        total_n = chain_n + chain_rem_n
        if total_n > max_dist:
            max_dist = total_n
            max_n = chain[0]
        for i in range(chain_n):
            dist_dict[int(chain[i])] = total_n - i
        index = index + 1
        while index in dist_dict:
            index = index + 1
    return((max_dist,max_n))

def pe_15(n_1,m_1):
    n = n_1 + 1
    m = m_1 + 1
    latt_n = np.zeros((n,m))
    latt_n[0,1:] = np.ones(m-1)
    for i in range(1,n):
        for j in range(i,m):
            if i == j:
                latt_n[i,j] = 2*latt_n[i-1,j]
            else:
                latt_n[i,j] = latt_n[i-1,j] + latt_n[i,j-1]
    return(latt_n[n-1,m-1])

def pe_16(n):
    n_dig = int(n*np.log10(2)) + 1
    digits = np.zeros(n_dig)
    digits[0] = 1
    high_dig = 1
    for i in range(n):
        digits[0:high_dig] = digits[0:high_dig]*2
        carry = 0
        for j in range(high_dig):
            numb = carry + digits[j]
            digits[j] = numb%10
            carry = numb//10
        if carry > 0:
            high_dig = high_dig + 1
            digits[high_dig-1] = carry
    return(np.sum(digits))

def pe_17():
    n_digits_letters = [3,3,5,4,4,3,5,5,4]#one,two,...,nine
    n_digits_sum = sum(n_digits_letters)
    
    n_teen_letters = [6,6,8,8,7,7,9,8,8]#eleven,twelve,...,nineteen
    n_teen_sum = sum(n_teen_letters)
    
    n_ten = 3
    n_tens_letters = [6,6,5,5,5,7,6,6]#twenty, ... ,ninety
    n_tens_sum = sum(n_tens_letters)
    
    n_hundred = 7 #hundred
    n_thousand = 8 #thousand
    n_and = 3
    
    n_2digits = n_digits_sum + n_ten + n_teen_sum + 10*n_tens_sum + 8*n_digits_sum
    n_3digits = n_2digits + (n_digits_sum + 9*n_hundred) + (9*n_2digits + 99*(n_digits_sum + 9*n_hundred + 9*n_and)) + 3 + n_thousand

    return(n_3digits)

def pe_18(pyramid):
    def prepare_arg_18(pyramid):
        pyramid = pyramid.split('\n')
        n = len(pyramid)
        triangle = [None]*n
        for i in range(n):
            triangle[i] = list(map(int,pyramid[i].split(' ')))
        return(triangle)
    triangle = prepare_arg_18(pyramid)
    n = len(triangle)
    max_p = [0]*n
    for i in range(n-1):
        max_p[i] = [0]*(i+1)
    max_p[n-1] = triangle[n-1]
    for i in range(n-2,-1,-1):
        for j in range(i+1):
            max_p[i][j] = triangle[i][j] + max(max_p[i+1][j],max_p[i+1][j+1])
    return(max_p[0][0])

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

def pe_20(n):
    log_sum = 0
    for i in range(2,n+1):
        log_sum = log_sum + math.log10(i)
    n_dig = int(log_sum) + 1
    digits = np.zeros(n_dig)
    digits[0] = 1
    max_dig = 1
    for i in range(2,n+1):
        digits[:max_dig] = i*digits[:max_dig]
        carry = 0
        for j in range(max_dig):
            total = carry + digits[j]
            carry = total//10
            digits[j] = total%10
        while carry > 0:
            max_dig = max_dig + 1
            digits[max_dig-1] = carry%10
            carry = carry//10
    return(np.sum(digits))


if __name__ == '__main__':
    completed = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
    inputs = {1:(3,5,1000),2:(4000000,),3:(600851475143,),4:(),5:(20,),6:(100,),7:(10001,),8:(PE_8_STRING,),9:(1000,),10:(2000000,),11:(PE_11_STRING,),12:(500,),
13:(PE_13_STRING,),14:(1000000,),15:(20,20),16:(1000,),17:(),18:(PE_18_STRING,),19:(),20:(100,)}
    total_time = 0
    for i in completed:
        pe_func = "pe_" + str(i)
        args = inputs[i]
        exec(f"x = {pe_func}")

        start = timeit.default_timer()
        res = x(*args)
        end = timeit.default_timer()
        total_time = total_time + end-start
        print("Problem: " + str(i))
        print("Result: " + str(res))
        print("Time: " + str(end-start))
    print("Total Time: " + str(total_time))
    print("Average Time: " + str(total_time/len(completed)))