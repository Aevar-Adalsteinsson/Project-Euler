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
    for i in np.arange(10):
        s = s + str(digits[i])
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

def pe_21(n):
    primes = pehelperfunctions.gen_primes(n+1)
    n_p = len(primes)
    div_sum = np.zeros(n,dtype = int)
    divisors = np.zeros(n_p,dtype = int)
    for i in range(2,n+1):
        cand = i
        prime_index = 0
        while cand != 1:
            prime = primes[prime_index]
            while cand%prime == 0:
                cand = cand//prime
                divisors[prime_index] = divisors[prime_index] + 1
            prime_index = prime_index + 1
        pos_index = np.where(divisors>0)
        divisors_pos = divisors[pos_index]
        prime_key = primes[pos_index]
        div_sum[i-1] = pehelperfunctions.divisor_sum(divisors_pos,prime_key,i)
        divisors[:prime_index] = np.zeros(prime_index,dtype = int)
    amic_sum = 0
    for i in range(2,n+1):
        i_sum = div_sum[i-1]
        if i_sum - 1 < n:
            amic_can = div_sum[i_sum-1]
            if amic_can == i and i < i_sum:
                amic_sum = amic_sum + i + i_sum
    return(amic_sum)

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

def pe_23():
    n = 28123
    primes = pehelperfunctions.gen_primes(n+1)
    n_p = len(primes)
    div_sum = np.zeros(n,dtype = int)
    divisors = np.zeros(n_p,dtype = int)
    for i in range(2,n+1):
        cand = i
        prime_index = 0
        while cand != 1:
            prime = primes[prime_index]
            while cand%prime == 0:
                cand = cand//prime
                divisors[prime_index] = divisors[prime_index] + 1
            prime_index = prime_index + 1
        pos_index = np.where(divisors>0)
        divisors_pos = divisors[pos_index]
        prime_key = primes[pos_index]
        div_sum[i-1] = pehelperfunctions.divisor_sum(divisors_pos,prime_key,i)
        divisors[:prime_index] = np.zeros(prime_index,dtype = int)
    abun_index = np.where((div_sum-np.arange(1,n+1))>0)
    abun = np.arange(1,n+1)[abun_index]
    abun_sum = np.arange(1,n+1)
    for i in abun:
        for j in abun:
            if i + j <= n:
                abun_sum[i+j-1] = 0
    return(np.sum(abun_sum))

def pe_24(n,m):
    #only works for small n and m
    perm = np.zeros(m,dtype = int)
    rank_rem = n-1
    nums = np.arange(m)
    for i in range(m):
        fact_i = math.factorial(m-1-i)
        quotient = rank_rem//fact_i
        rank_rem = rank_rem%fact_i
        perm[i] = nums[quotient]
        nums = np.delete(nums,quotient)
    s = ""
    for p in perm:
        s = s + str(p)
    return(s)

def pe_25(n):
    fib_1 = 1
    fib_2 = 1
    fib_n = 2
    while int(math.log10(fib_2))+1 < n:
        temp = fib_1 + fib_2
        fib_1 = fib_2
        fib_2 = temp
        fib_n = fib_n + 1
    return(fib_n)

def pe_27(n,m):
    # n^2 + an + b
    # |a|<n, |b|<= m
    primes = pehelperfunctions.gen_primes(m)
    max_prime = primes[len(primes)-1]
    primes_n = len(primes)
    max_chain = 0
    for b in primes:
        for a in range(-b+1,n):
            n = 1
            chain_n = 1
            prime_cand = n**2 + a*n + b
            if prime_cand < prime_cand:
                primes = pehelperfunctions.gen_additional_primes_2(max_prime*5,primes)#5 arbitrary
                primes_n = len(primes)
                max_primes = primes[primes_n-1]
            while prime_cand in primes:#could be improved
                chain_n = chain_n +1
                n = n+1
                prime_cand = n**2 + a*n + b#could be +a -1 + 2n, (n-1)(n-1) = n^2 -2n+1
                if prime_cand < prime_cand:
                    primes = pehelperfunctions.gen_additional_primes_2(max_prime*5,primes)#5 arbitrary
                    primes_n = len(primes)
                    max_primes = primes[primes_n-1]
            if chain_n > max_chain:
                max_pair = a*b
                max_chain = chain_n
    return(max_pair)

def pe_28(n):
    #right upper odd^2
    #left lower  even^2 + 1
    #right lower odd*even + 1
    #left upper  even*odd + 1
    
    diagonal_sum = np.sum(np.arange(1,n+1,2)**2)
    diagonal_sum = diagonal_sum + np.sum(np.arange(2,n+1,2)**2+np.ones((n-1)//2))
    main_diag = np.arange(1,n)*np.arange(2,n+1) + np.ones(n-1)
    diagonal_sum = diagonal_sum + np.sum(main_diag)
    return(diagonal_sum)

def pe_29(n):
    nums = np.arange(2,n+1)
    distinct_powers = 0
    for i in range(len(nums)):
        powers = np.zeros(0,dtype = int)
        power = nums[i]
        if power > 0:
            curr_power = power
            exponent_power = 1
            while curr_power < n+1:
                nums[curr_power-2] = 0
                powers = np.append(powers,exponent_power*np.arange(2,n+1))
                curr_power = curr_power*power
                exponent_power = exponent_power + 1
            powers.sort()
            distinct_powers = distinct_powers + 1
            for i in range(1,len(powers)):
                if powers[i-1] != powers[i]:
                    distinct_powers = distinct_powers + 1
    return(distinct_powers)

def pe_30():
    power_sum = 0
    for i in range(2,354294):
        digit_sum = 0
        i_og = i
        rem = i%10
        i = i//10
        while i > 0:
            digit_sum = digit_sum + rem**5
            rem = i%10
            i = i//10
        digit_sum = digit_sum + rem**5
        if digit_sum == i_og:
            power_sum = power_sum + i_og
    return(power_sum)

def pe_31(coins,amount):
    #every coin must be a multiple of last coin
    #coins and amount must be integers
    #coins in increasing order
    n = len(coins)
    if n == 1:
        return(1)
    if n == 2:
        return(amount//coins[1] + 1)
    coin = coins[n-1]
    sums = 0
    for i in range(amount//coin+1):
        sums_i = pe_31(coins[:(n-1)],amount-i*coin)
        sums = sums + sums_i
    return(sums)

def pe_32():
    digits = np.zeros(9,dtype = int)
    pan_prods = np.empty(0,dtype = int)
    for i in range(2,99):
        i_dig = int(math.log10(i)) + 1
        if i_dig == 1:
            digits[0] = i
        else:
            digits[0] = i%10
            quotient = i//10
            if quotient == 0 or quotient == digits[0]:
                continue
            digits[1] = quotient
        #lower bound for j = 10**(4-i_dig)
        #upper bound for j = 10**5/i
        for j in range(10**(4-i_dig),10000//i+1):
            digits[i_dig:] = np.zeros(9-i_dig,dtype = int)
            
            j2 = j
            digit_index = i_dig-1
            flag = False
            while j2>0:
                digit_index = digit_index + 1
                rem = j2%10
                j2 = j2//10
                if rem == 0 or rem in digits[:digit_index]:#pandigital condition
                    flag = True
                    break
                digits[digit_index] = rem
            if flag:
                continue
            product = i*j
            
            prod_dig = int(math.log10(product)) + 1
            if prod_dig+1+4 != 9:
                continue
            
            product2 = product
            while product2>0:
                digit_index = digit_index + 1
                rem = product2%10
                product2 = product2//10
                if rem == 0 or rem in digits[:digit_index]:#pandigital condition
                    flag = True
                    break
                digits[digit_index] = rem
            if flag:
                continue
            if product not in pan_prods:
                pan_prods = np.append(pan_prods,np.array([product]))
    return(np.sum(pan_prods))

def pe_34():
    fact = [math.factorial(x) for x in range(10)]
    max_8 = fact[8]*6 #8!*6 has 6 digits and 8!*7 has 6 digits
    fact_digit_sum = 0
    i = 10
    while i < 2540160:# for i in range(10,2540160):
        digits = []
        max_digit = 0
        i_1 = i
        n_9 = 0
        while i_1 > 0:
            digit = i_1%10
            if digit > max_digit:
                max_digit = digit
            if digit == 9:
                n_9 += 1
            digits.append(digit)
            i_1 = i_1//10
        if max_digit == 9:
            if i < fact[9]:
                i = i+1
                continue
            if i > n_9*fact[9] + (7-n_9)*fact[8]:#i needs to have more digits that are 9
                pow_10 = 1
                while i%(10**pow_10) == 9:
                    pow_10 += 1
                i = i - i%(10**pow_10) + 10**pow_10 - 1
        else:
            if i > max_8:
                i = i - i%10+9#
                continue
        fact_sum = 0
        for j in digits:
            fact_sum += fact[j]
        if fact_sum == i:
            fact_digit_sum += i
        i = i+1
    return(fact_digit_sum)

def pe_35(n):
    primes = pehelperfunctions.gen_primes(n)
    n_primes = len(primes)
    max_digits = int(math.log10(primes[len(primes)-1])) + 1
    digits = np.zeros(max_digits,dtype=int)
    circ_dict = {2:True,3:True,5:True,7:True}
    n_circ = 4
    for p in primes[4:]:
        p_ndig = int(math.log10(p)) + 1
        p_dig, p_ind = pehelperfunctions.get_digits(digits[:p_ndig],p)
        flag = False
        for digit in p_dig:
            if digit%2 == 0 or digit == 5:
                flag = True
                break
        if flag:
            continue
        flag = False
        
        circ_cand = np.zeros(p_ndig)
        circ_cand[0] = p
        min_circ = math.inf
        for i in range(1,p_ndig):
            p_cand = 0
            for j in range(p_ndig):
                p_cand = p_cand + p_dig[(j+i)%p_ndig]*(10**j)
            min_circ = min(min_circ,p_cand)
            circ_cand[i] = p_cand
            if not pehelperfunctions.bin_search_check(primes,p_cand,0,n_primes):
                flag = True
                break
        if flag:
            continue
        if min_circ not in circ_dict:
            for circ in circ_cand:
                circ_dict[circ] = True
    return(len(circ_dict))

def pe_36(n):
    pal_sum = 0
    for i in np.arange(1,n):
        if pehelperfunctions.is_palindrome(i):
            bin_str = bin(i)[2:]
            if pehelperfunctions.is_palindrome_str(bin_str):
                pal_sum = pal_sum + i
                #print(i)
    return(pal_sum)

def pe_37():
    n = 1000000
    primes = pehelperfunctions.gen_primes(n)
    dig1_primes = [2,3,5,7]
    trunc_sum = 0
    for p in primes[4:]:
        p_n = int(math.log10(p))+1
        digits = pehelperfunctions.get_digits_2(p)
        
        if digits[0] not in dig1_primes:
            continue
        if digits[p_n-1] not in dig1_primes[1:]:
            continue
        flag = False
        for i in np.arange(1,p_n-1):
            if digits[i]%2 == 0:
                flag = True
                break
        if flag:
            continue
        p_left = p
        p_right = p
        for i in np.arange(p_n-1):
            p_left = p_left % 10**(p_n-i-1)
            p_right = p_right//10
            if p_left not in primes or p_right not in primes:
                flag = True
                break
        if flag:
            continue
        trunc_sum = trunc_sum + p
    return(trunc_sum)

def pe_38():
    #9(1,2,3,4,5) = 918273645 exists so the leading digit must be 9
    pandig_max = 918273645
    for i in np.arange(2,5):
        #i number of digit
        for n in np.arange(9*(10**i)+1,10**(i+1)):
            digits = pehelperfunctions.get_digits_2(n)
            if 0 in digits:
                continue
            if len(digits) != len(set(digits)):
                continue
            s = ""#
            mult_ind = 1
            while len(s)<9:
                s = s + str(n*mult_ind)
                mult_ind = mult_ind + 1
            s_len = len(s)
            if s_len != 9 or "0" in s or s_len != len(set(s)):
                continue
            m = int(s)
            if m > pandig_max:
                pandig_max = m
    return(pandig_max)

def pe_39(n):
    int_tri_max = 0
    max_i = 0
    for i in np.arange(6,n+1):
        pyth_n = 0
        for a in np.arange(1,i//3):
            r = i-a
            b = (r**2-a**2)/(2*r)
            c = r-b
            if b == int(b):
                pyth_n = pyth_n + 1
        if pyth_n > int_tri_max:
            int_tri_max = pyth_n
            max_i = i
    return(max_i)

def pe_40():
    def get_dec_digit(n):
        if n < 10:
            return(n)
        n = n - 10
        dig = 2
        while True:
            tot_dig = dig*9*(10**(dig-1))
            if tot_dig > n:
                break
            n = n-tot_dig
            dig = dig + 1
        quot = n//dig
        rem = n%dig
    
        num = 10**(dig-1) + quot
        digit = num//10**(dig-1-rem)
        digit = digit%10
        return(digit)
    digs = 10**np.arange(7)
    prod = 1
    for dig in digs:
        prod = prod*get_dec_digit(dig)
    return(prod)

def pe_41():
    for m in np.arange(9,0,-1):
        digits = np.arange(m,0,-1)
        pandig = np.sum(10**np.arange(m-1,-1,-1)*digits)
        n = int(np.sqrt(pandig))+1
        primes = pehelperfunctions.gen_primes(n)
        count = 0
        bound = math.factorial(m)
        while count < bound:
            prev_digits = np.copy(digits)
            digits = pehelperfunctions.prev_pandigital(digits,m)
            diff = np.sum(10**np.arange(m-1,-1,-1)*(digits-prev_digits))
            pandig = pandig + diff
            count = count + 1
            flag = True
            for p in primes:
                if pandig%p == 0:
                    flag = False
                    break
            if flag:
                return(pandig)

def pe_42():
    f = open("pe_42_words.txt", "r")
    words = f.read()
    words = words.split(",")
    words = [word[1:-1] for word in words]

    max_tri = 0
    max_tri_n = 0
    tri = []
    tri_n = 0
    for word in words:
        val = 0
        for c in word:
            val += ord(c)-64
        while val > max_tri:
            max_tri_n += 1
            max_tri = max_tri_n*(max_tri_n+1)//2
            tri.append(max_tri)
        if val in tri:#binary search or turn tri into set for more efficiency
            tri_n += 1
    return(tri_n)

def pe_43():
    def digits_next(digits,ind):
        dig_sort = np.sort(digits[ind:])
        dig_sort = np.flip(dig_sort)
        digits = np.append(digits[:ind],dig_sort)
        digits = pehelperfunctions.next_pandigital(digits,len(digits))
        return(digits)
    pan_sum = 0.0
    digits = np.array([1,0,2,3,4,5,6,7,8,9],dtype = float)
    primes = np.array([2,3,5,7,11,13,17])
    highest = np.array([9,8,7,6,5,4,3,2,1,0],dtype = float)
    count = 0
    while not (highest == digits).all():
        flag = False
        for i in np.arange(7):
            ind = i+1
            num = digits[ind]*100 + digits[ind+1]*10 + digits[ind+2]
            if num%primes[i] != 0:
                digits = digits_next(digits,i+4)
                flag = True
                break
        if flag:
            continue
        pan_sum = pan_sum + np.sum(10**np.arange(10-1,-1,-1)*digits)
        digits = pehelperfunctions.next_pandigital(digits,len(digits))
    return(pan_sum)  

def pe_44():
    m = 1.0
    
    while True:
        p = m*(3*m-1)/2 
        upper = int((1+np.sqrt(1+24*p))/6)+1
        for i in np.arange(1,upper):
            n = (2*p - 3*i*i + i)/(6*i)
            if n.is_integer() and n != 0:
                n_i = n+i
                
                p_n = n*(3*n-1)/2
                p_n_i = n_i*(3*n_i-1)/2
            
                p_sum = p_n_i + p_n
            
                p_sum_n = (1+np.sqrt(1+24*p_sum))/6
                if p_sum_n.is_integer():
                    return(p)
        m = m + 1

def pe_45():
    n = 144.0
    while True:
        hex_n = n*(2*n-1)
        pent_n = (1+np.sqrt(1+24*hex_n))/6
        if not pent_n.is_integer():
            n = n+1
            continue
        tri_n = (-1+np.sqrt(1+8*hex_n))/2
        if tri_n.is_integer():
            return(hex_n)
        n = n+1

def pe_46():
    primes = pehelperfunctions.gen_primes(100000)
    p_n = len(primes)
    n = 35
    while True:
        if n in primes:
            n = n+2
            continue
        ind = 0
        flag = False
        while ind < p_n:
            p = primes[ind]
            if p >= n:
                break
            square = (n-p)/2
            if np.sqrt(square).is_integer():
                flag = True
                break
            ind = ind + 1
        if flag:
            n = n+2
            continue
        return(n)

def pe_47():
    distinct_n = 0
    n = 4
    primes = [2,3,5,7]
    next_prime = 5
    next_prime_ind = 2
    primes_ind = {2:0,3:1}
    max_prime = primes[len(primes)-1]
    while distinct_n < 4:
        if next_prime - (n-1) + distinct_n <= 3:
            distinct_n = 0
            n = next_prime + 1
            prev_prime = next_prime
            next_prime_ind += 1
            next_prime = primes[next_prime_ind]
            while next_prime - prev_prime < 5:
                if next_prime >= max_prime:
                    primes, primes_ind = pehelperfunctions.gen_additional_primes(n*5,primes,primes_ind)#5 arbitrarily chosen
                    max_prime = primes[len(primes)-1]
                n = next_prime+1
                prev_prime = next_prime
                next_prime_ind += 1
                next_prime = primes[next_prime_ind]
                
            if next_prime >= max_prime:
                primes, primes_ind = pehelperfunctions.gen_additional_primes(n*5,primes,primes_ind)#5 arbitrarily chosen
                max_prime = primes[len(primes)-1]
        if max_prime < n:
            primes, primes_ind = pehelperfunctions.gen_additional_primes(n*5,primes,primes_ind)#5 arbitrarily chosen
            max_prime = primes[len(primes)-1]
        prime_div_n = pehelperfunctions.get_prime_divisor_n(n,primes[:(next_prime_ind+1)])
        if prime_div_n >= 4:
            distinct_n += 1
        else:
            distinct_n = 0
        n = n+1
    return(n-4)

def pe_48(n):
    digits = np.zeros(10,dtype = int)
    for i in np.arange(1,n+1):
        i_digits = np.zeros(10,dtype = int)
        ind = 9
        k = i
        while k > 0 and ind >= 0:
            i_digits[ind] = k%10
            k = k//10
            ind -= 1
        for j in np.arange(i-1):
            i_digits = i_digits*i
            carry = 0
            for l in np.arange(10):
                i_digits[9-l] = i_digits[9-l] + carry
                carry = i_digits[9-l]//10
                i_digits[9-l] = i_digits[9-l]%10
        digits = digits + i_digits
    carry = 0
    for l in np.arange(10):
        digits[9-l] = digits[9-l] + carry
        carry = digits[9-l]//10
        digits[9-l] = digits[9-l]%10
    s = ""
    for digit in digits:
        s = s + str(digit)
    return(s)

def pe_49():
    primes = pehelperfunctions.gen_primes(10000)
    ind = np.searchsorted(primes,1000)
    primes = primes[ind:]
    prime_n = len(primes)
    for i in np.arange(prime_n-3):
        p_1 = primes[i]
        digits = pehelperfunctions.get_digits_2(p_1)
        digits = np.sort(digits)
        for j in np.arange(i+1,prime_n-2):
            arith_n = 2
            p_2 = primes[j]
            digits_j = np.sort(pehelperfunctions.get_digits_2(p_2))
            inc = p_2 - p_1
            arith_concat = str(p_1) + str(p_2)
            if (digits_j == digits).all():
                p_curr = p_2
                while arith_n < 3:
                    
                    p_curr = p_curr + inc
                    digits_curr = np.sort(pehelperfunctions.get_digits_2(p_curr))
                    prime_ind = np.searchsorted(primes,p_curr)
                    if p_curr < 10000 and (digits_curr == digits).all() and p_curr == primes[prime_ind]:
                        arith_n = arith_n + 1
                        arith_concat = arith_concat + str(p_curr)
                    else:
                        break
                if arith_n == 3:
                    if p_1 == 1487:
                        continue
                    return(arith_concat)

def pe_50(n):
    primes = pehelperfunctions.gen_primes(n)
    primes_n = len(primes)

    con_p_sum = np.zeros(n+1,dtype = int)
    p_ind = 0
    max_con = 0
    max_p = 0
    for i in np.arange(primes_n):
        p = primes[primes_n-1-i]
        con_sum = 0
        con_n = 0
        p_ind = 0
        while con_sum < p:
            con_sum += primes[p_ind]
            p_ind += 1
            con_n += 1
        if con_n < max_con:
            return(max_p)
        high_ind = p_ind
        low_ind = 0
        while con_sum != p and con_n > max_con:
            if con_sum > p:
                con_sum = con_sum - primes[low_ind]
                con_n = con_n -1
                low_ind += 1
            else:
                con_sum = con_sum + primes[high_ind]
                con_n = con_n +1
                high_ind +=1
        if con_sum == p:
            if con_n > max_con:
                max_con = con_n
                max_p = p
    return(max_p)

def pe_51():
    n = 1000000
    primes = pehelperfunctions.gen_primes(n)
    
    
    max_rep = 0
    for p in primes[4:]:
        digits_n = int(math.log10(p))+1
        
        dig_012 = np.zeros(3,dtype = int)
        dig_012_place = [[],[],[]]
        p_dig = p #replacing the last digit can only produce at most 4 prime digit replacements
        dig_ind = 0
        while p_dig != 0:
            dig = p_dig%10
            if dig < 3:
                dig_012[dig] = dig_012[dig] + 1
                dig_012_place[dig].append(dig_ind)
            p_dig = p_dig//10
            dig_ind = dig_ind + 1
        last_dig = p%10
        if last_dig < 3:
            dig_012[last_dig] = dig_012[last_dig] - 1
        

        for i in np.arange(len(dig_012)):
            dig_i = dig_012[i]
            if dig_i == 0:
                continue
            
            if last_dig == i:
                place_inc = 1
            else:
                place_inc = 0
            for j in np.arange(1,2**dig_i):
                indices = list(format(j,'#0' + str(dig_i+2) + 'b')[2:])
                indices = list(map(int, indices))
                
                
                increment = 0
                for k in np.arange(len(indices)):
                    index = indices[k]
                    if index == 1:
                        increment = increment + 10**dig_012_place[i][k + place_inc]
                    
                

                p_cand = p - i*increment
                
                p_cand_ind = 0
                if digits_n-1 in dig_012_place[i]:#candidates must have the same number of digits

                    p_cand = p_cand + increment
                    p_cand_ind = p_cand_ind + 1
                
                p_count = 0
                while p_cand_ind < 10:
                    if p_cand in primes:
                        p_count = p_count + 1
                    p_cand = p_cand + increment
                    p_cand_ind = p_cand_ind + 1
                if p_count > max_rep:
                    max_rep = p_count
                    if p_count == 8:
                        return(p)

def pe_52():
    for i in np.arange(3,7):
        for j in np.arange(10**i,10**(i+1)//6+1):
            j_digits = pehelperfunctions.get_digits_2(j)
            j_digits.sort()
            flag = True
            for k in np.arange(2,7):
                digits = pehelperfunctions.get_digits_2(k*j)
                digits.sort()
                if not all(j_digits == digits):
                    flag = False
                    break
            if flag:
                return(j)

def pe_53():
    m = 100
    log_n = np.log(np.arange(1,m+1))
    log_fact_n = np.zeros(m+1)
    for i in np.arange(1,m+1):
        log_fact_n[i] = log_fact_n[i-1]+log_n[i-1]
    mill_log = np.log(10**6)
    count = 0
    for n in np.arange(1,m+1):
        for r in np.arange(n):#it is possible to reduce the number by half by use of symmetry
            log_fact = log_fact_n[n]-log_fact_n[r]-log_fact_n[n-r]
            if log_fact>mill_log:
                count = count + 1
    return(count)

def pe_54():
    def is_flush(hand_1,hand_2):
        sort_1 = hand_1[0][1]
        sort_2 = hand_2[0][1]
        flag_1 = True
        flag_2 = True
        for i in range(1,5):
            sort_1i = hand_1[i][1]
            sort_2i = hand_2[i][1]
            if sort_1i != sort_1:
                flag_1 = False
            if sort_2i != sort_2:
                flag_2 = False
        flush_1 = flag_1
        flush_2 = flag_2
        return((flush_1,flush_2))
    def is_straight(rank_1,rank_2,rank):
        low_1 = rank_1[0]
        low_2 = rank_2[0]
        flag_1 = True
        flag_2 = True
        for i in range(1,5):
            rank_1i = rank_1[i]
            rank_2i = rank_2[i]
            if rank_1i != low_1+i:
                if i == 4 and rank_1i == 12 and low_1 == 0:
                    pass
                else:
                    flag_1 = False
            if rank_2i != low_2+i:
                if i == 4 and rank_2i == 12 and low_2 == 0:
                    pass
                else:
                    flag_2 = False
        straight_1 = flag_1
        straight_2 = flag_2
        return((straight_1,straight_2))
    def get_pairs(rank_1,rank_2):
        #all ranks and their multiplicity, one card, pair,trips and quads
        pairs_1 = []
        pairs_2 = []
        
        prev_rank_1 = rank_1[0]
        prev_rank_2 = rank_2[0]
        count_1 = 1
        count_2 = 1
        for i in range(1,5):
            rank_i1 = rank_1[i]
            rank_i2 = rank_2[i]
            if rank_i1 == prev_rank_1:
                count_1 += 1
            else:
                pairs_1.append((count_1,prev_rank_1))
                count_1 = 1
            if rank_i2 == prev_rank_2:
                count_2 += 1
            else:
                pairs_2.append((count_2,prev_rank_2))
                count_2 = 1
            prev_rank_1 = rank_i1
            prev_rank_2 = rank_i2
        pairs_1.append((count_1,prev_rank_1))
        pairs_2.append((count_2,prev_rank_2))
        pairs_1.sort(reverse = True)
        pairs_2.sort(reverse = True)
        return((pairs_1,pairs_2))
        
    f = open("pe_54_poker.txt", "r")

    poker = f.read()
    poker = poker.split("\n")
    poker = poker[:(len(poker)-1)]
    
    rank = {'2':0,'3':1,'4':2,'5':3,'6':4,'7':5,'8':6,'9':7,'T':8,'J':9,'Q':10,'K':11,'A':12}
    n = len(poker)
    p1_wins = 0
    for i in range(n):
        hands = poker[i]
        hands = hands.split(" ")
        hand_1 = hands[:5]
        hand_2 = hands[5:]
        
        rank_1 = []
        rank_2 = []
        for j in range(5):
            rank_1.append(rank[hand_1[j][0]])
            rank_2.append(rank[hand_2[j][0]])
        rank_1.sort()
        rank_2.sort()
        
        flush_1, flush_2 = is_flush(hand_1,hand_2)
        straight_1, straight_2 = is_straight(rank_1,rank_2,rank)
        pairs_1, pairs_2 = get_pairs(rank_1,rank_2)
        
        #straigt flush and royal flush
        if flush_1 and straight_1:
            if flush_2 and straight_2 and rank_1[4] <= rank_2[4]:
                continue
            p1_wins += 1
            continue
        if flush_2 and straight_2:
            continue
        #four of a kind
        if pairs_1[0][0] == 4:
            if pairs_2[0][0] == 4 and pairs_1[0][1] <= pairs_2[0][1]:
                continue
            p1_wins += 1
            continue
        if pairs_2[0][0] == 4:
            continue
        #full house
        if len(pairs_1) == 2:
            if len(pairs_2) == 2 and pairs_1[0][1] < pairs_2[0][1]:#cant have two three of the kind of the same rank
                continue
            p1_wins += 1
            continue
        if len(pairs_2) == 2:
            continue
        #print("flush")
        #flush
        if flush_1:#can be improved with more rank comparisons
            if flush_2 and rank_1[4] <= rank_2[4]:
                continue
            p1_wins += 1
            continue
        if flush_2:
            continue
        #straight
        if straight_1:
            if straight_2 and rank_1[4] <= rank_2[4]:
                continue
            p1_wins += 1
            continue
        if straight_2:
            continue
        #three of a kind
        if pairs_1[0][0] == 3:
            if pairs_2[0][0] == 3:
                bool_1 = pairs_1[0][1] < pairs_2[0][1]
                bool_2 = pairs_1[0][1] == pairs_2[0][1] and pairs_1[1][1] < pairs_2[1][1]
                bool_3 = pairs_1[0][1] == pairs_2[0][1] and pairs_1[1][1] == pairs_2[1][1] and pairs_1[2][1] <= pairs_2[2][1]
                if bool_1 or bool_2 or bool_3:
                    continue
                p1_wins += 1
                continue
            else:
                p1_wins += 1
                continue
        if pairs_2[0][0] == 3:
            continue
        #two pairs
        if pairs_1[0][0] == 2 and pairs_1[1][0] == 2:
            if pairs_2[0][0] == 2 and pairs_2[1][0] == 2:
                bool_1 = pairs_1[0][1] < pairs_2[0][1]
                bool_2 = pairs_1[0][1] == pairs_2[0][1] and pairs_1[1][1] < pairs_2[1][1]
                bool_3 = pairs_1[0][1] == pairs_2[0][1] and pairs_1[1][1] == pairs_2[1][1] and pairs_1[2][1] <= pairs_2[2][1]
                if bool_1 or bool_2 or bool_3:
                    continue
                p1_wins += 1
                continue
            else:
                p1_wins += 1
                continue
        if pairs_2[0][0] == 2 and pairs_2[1][0] == 2:
            continue
        #pair
        if pairs_1[0][0] == 2:
            if pairs_2[0][0] == 2:
                bool_1 = pairs_1[0][1] < pairs_2[0][1]
                bool_2 = pairs_1[0][1] == pairs_2[0][1] and pairs_1[1][1] < pairs_2[1][1]
                bool_3 = pairs_1[0][1] == pairs_2[0][1] and pairs_1[1][1] == pairs_2[1][1] and pairs_1[2][1] < pairs_2[2][1]
                bool_4 = pairs_1[0][1] == pairs_2[0][1] and pairs_1[1][1] == pairs_2[1][1] and pairs_1[2][1] == pairs_2[2][1]
                bool_4 = bool_4 and pairs_1[3][1] <= pairs_2[3][1]
                if bool_1 or bool_2 or bool_3 or bool_4:
                    continue
                p1_wins += 1
                continue
            else:
                p1_wins += 1
                continue
        if pairs_2[0][0] == 2:
            continue
        #high card
        bool_0 = rank_1[4] < rank_2[4]
        bool_1 = rank_1[4] == rank_2[4] and rank_1[3] < rank_2[3]
        bool_2 = rank_1[4] == rank_2[4] and rank_1[3] == rank_2[3] and rank_1[2] < rank_2[2]
        bool_3 = rank_1[4] == rank_2[4] and rank_1[3] == rank_2[3] and rank_1[2] == rank_2[2] and rank_1[1] < rank_2[1]
        bool_4 = rank_1[4] == rank_2[4] and rank_1[3] == rank_2[3] and rank_1[2] == rank_2[2] and rank_1[1] == rank_2[1] and rank_1[0] <= rank_2[0]
        if bool_0 or bool_1 or bool_2 or bool_3 or bool_4:
            continue
        else:
            p1_wins += 1
    return(p1_wins)

def pe_55():
    def reverse_num(digits):
        n = len(digits)
        rev = np.zeros(n)
        for i in np.arange(n):
            rev[i] = digits[n-1-i]
        return(rev)
    lych_n = 0
    for i in np.arange(5,10000):
        count = 0
        lychrel_cand = pehelperfunctions.get_digits_2(i)
        flag = True
        while count <= 50:
            rev = reverse_num(lychrel_cand)
            lychrel_cand = pehelperfunctions.digits_sum(lychrel_cand,rev)
            if pehelperfunctions.is_palindrome_digits(lychrel_cand):
                flag = False
                break
            count = count + 1
        if flag:
            lych_n = lych_n + 1
    return(lych_n)

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

def pe_58():
    n = 10**3
    primes = pehelperfunctions.gen_primes(n)

    total = 1
    n_p = 0
    m = 1
    while True:
        p_1 = 2*m*(2*m+1) + 1
        p_2 = (2*m+1)**2
        p_3 = (2*m)**2+1
        p_4 = (2*m)*(2*m-1) + 1
        
        if pehelperfunctions.is_prime(primes,p_1):
            n_p = n_p + 1
        if pehelperfunctions.is_prime(primes,p_3):
            n_p = n_p + 1
        if pehelperfunctions.is_prime(primes,p_4):
            n_p = n_p + 1
        total = total+4
        if n_p/total < 0.1:
            return(2*m+1)
        m = m+1

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

def pe_61():
    def cyclic_6(cycle,cycle_dict,num_rem,last_2):
        m = len(num_rem)
        if m == 0:
            n_1 = cycle[0]
            n_2 = cycle[len(cycle)-1]
            if n_1//100 == n_2%100:
                return(np.sum(cycle))
            return(None)
    
        for i in np.arange(m):
            num_type = num_rem[i]
            k = last_2*100
            n_cand = num_type-1 + np.sqrt(num_type**2 -2*num_type + 1 + 8*k + 8*num_type*k)
            n_cand = n_cand/(2 + 2*num_type)
            n_cand = int(n_cand)
        
            n_2 = int((n_cand+1)*((n_cand+2)/2+num_type*n_cand/2))
        
            if n_2//100 == last_2 and (n_2%100)//10 != 0:
                cycle_dict[num_type] = n_2
                cycle_2 = np.append(cycle,np.array([n_2],dtype = int))
                num_rem_2 = np.delete(num_rem,i)
            
                val = cyclic_6(cycle_2,cycle_dict,num_rem_2,n_2%100)
                if val is not None:
                    return(val)
        return(None)
    
    
    for i in np.arange(18,58):
        cycle = np.zeros(1,dtype = int)
        cycle_dict = {}
        cycle_ind = 0
        num_type = 5
        
        n = int(i*((i+1)/2+num_type*(i-1)/2))
        last_2 = n%100
        if last_2//10 == 0:
            continue
        cycle[cycle_ind] = n
        cycle_dict[cycle_ind] = num_type
        cycle_ind = cycle_ind + 1
        val = cyclic_6(cycle,cycle_dict,np.arange(5),last_2)
        if val is not None:
            return(val)

def pe_62():
    def get_dig_occ(digits):
        #number of digit occurrences
        dig_occ = [0]*10
        n = len(digits)
        for i in np.arange(n):
            dig = digits[i]
            dig_occ[dig] = dig_occ[dig] + 1
        return(dig_occ)
    min_cube = math.inf
    for i in np.arange(3,20):
        flag = False
        digits = [0]*(i+1)
        
        low = int(10**(i/3))+1
        high = int(10**((i+1)/3))
    
    
        dig_occ = []
        for j in np.arange(low,high+1):
            digits = pehelperfunctions.get_digits_3(j)
            digits = pehelperfunctions.digits_prod(pehelperfunctions.digits_prod(digits,digits),digits)
            dig_occ.append(get_dig_occ(digits))
        dig_occ.sort()
        prev = dig_occ[0]
        cub_per_n = 1
        for j in np.arange(1,len(dig_occ)):
            curr = dig_occ[j]
            if prev == curr:
                cub_per_n = cub_per_n + 1
            else:
                cub_per_n = 1
            prev = curr
            if cub_per_n > 3:
                if cub_per_n == 5:
                    flag = True
                    for k in np.arange(low,high+1):
                        digits = pehelperfunctions.get_digits_3(k)
                        digits = pehelperfunctions.digits_prod(pehelperfunctions.digits_prod(digits,digits),digits)
                        occ = get_dig_occ(digits)
                        if occ == curr:
                            if k < min_cube:
                                min_cube = k
        if flag:
            break
    return(int(min_cube)**3)

def pe_63():
    count = 0
    for i in np.arange(1,10):
        t = 1/(1-math.log10(i))
        count = count + int(t)
    return(count)

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

def pe_65(n):
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
    
    plus_term = 2
    periods = [0]*(n-1)
    for i in range(n-1):
        if i%3 == 1:
            periods[i] = (i//3+1)*2
        else:
            periods[i] = 1
    nom,denom = rat_approx(plus_term,periods)
    digit_sum = 0
    while nom > 0:
        digit_sum += nom%10
        nom = nom//10
    return(digit_sum)

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

def pe_67():
    def process_67():
        f = open("pe_67_triangle.txt", "r")
        pyramid = f.read()
        pyramid = pyramid.split('\n')

        n = len(pyramid)
        pyramid = pyramid[:(n-1)]
        n = n-1
        triangle = []
        for i in range(len(pyramid)):
            tri = pyramid[i].split(" ")
            triangle.append([int(x) for x in tri])
        return(triangle)
    
    triangle = process_67()
    
    n = len(triangle)
    for i in range(n-2,-1,-1):
        m = len(triangle[i])
        for j in range(m):
            triangle[i][j] += max(triangle[i+1][j],triangle[i+1][j+1])
    return(triangle[0][0])

def pe_69(n):
    primes = pehelperfunctions.gen_primes(n)
    primes_n = len(primes)
    max_tot = 1
    max_tot_n = 1
    total = 2
    prime_div = [2]
    i = 0
    while total <= n:
        tot = pehelperfunctions.totient(prime_div,total)
        if total/tot > max_tot:
            max_tot = total/tot
            max_tot_n = total
        i += 1
        p = primes[i]
        total = total*p
        prime_div.append(p)
    return(max_tot_n)

def pe_71(d):
    primes = pehelperfunctions.gen_primes(d)
    val = d//7
    upper = 3*val
    for i in range(upper,0,-1):
        if np.gcd(i,7*val) == 1:
            closest = 3/7-i/(7*val)#good candidate
            closest_nd = (i,7*val)
            break

    for i in range(2,d+1):
        if i == 7:
            continue
        
        upper = i*3//7 
        if 3/7-upper/i > closest:
            continue
        i_div = pehelperfunctions.get_prime_divisor_simple(i,primes)
        for j in range(upper,0,-1):
            diff = 3/7-j/i
            if diff > closest:
                break
            is_coprime = True
            for prime in i_div:
                if j%prime == 0:
                    is_coprime = False
                    break
            if is_coprime:
                if diff < closest:
                    closest = diff
                    closest_nd = (j,i)
                break
    return(closest_nd[0])

def pe_72(d):
    #need nested loop because we overcount non reduce proper fraction by simply going through the primes
    #example: we overcount 6/30 since 2 and 3 is both factors of 6
    def nested_loop(prime_m,primes,factors,n):
        if len(factors)>0:
            prime_m.append(factors)
        if len(primes) == 0 or n < primes[0]:
            return(prime_m)
        
        for i in range(len(primes)):
            p = primes[i]
            k = n//int(p)-1
            #if len(factors) == 0:
            #    k = k-1
            if k == 0:
                break
            new_factors = [x for x in factors]
            new_factors.append(p)
            prime_m = nested_loop(prime_m,primes[(i+1):],new_factors,n//p)
        return(prime_m)
    
    all_frac = (d-1)*d//2
    primes = pehelperfunctions.gen_primes(d//2 + 1)
    non_red = 0
    
    prime_m = nested_loop([],primes,[],d)
    for i in range(len(prime_m)):
        prime_factors = prime_m[i]
        num = math.prod(prime_factors)
        if len(prime_factors)%2 == 1:
            pm = 1
        else:
            pm = -1
        k = d//int(num)-1          #numbers n <= d that satisfy gcd(n,num) = num^s for some s > 0 excluding p itself
        non_red += pm*k*(k+1)//2   #each multiple of p, say np, has n-1 non reduced fraction because of p 

    return(all_frac-non_red)

def pe_73(d):
    def nested_loop(prime_m,primes,factors,n):
        if len(factors)>0:
            prime_m.append(factors)
        if len(primes) == 0 or n < primes[0]:
            return(prime_m)
        
        for i in range(len(primes)):
            p = primes[i]
            k = n//int(p)-1
            #if len(factors) == 0:
            #    k = k-1
            if k == 0:
                break
            new_factors = [x for x in factors]
            new_factors.append(p)
            prime_m = nested_loop(prime_m,primes[(i+1):],new_factors,n//p)
        return(prime_m)
    all_frac = 0
    frac_n = 0
    primes = pehelperfunctions.gen_primes(d)
    for i in range(5,d+1):
        prime_factors = pehelperfunctions.get_prime_divisor_simple(i,primes)
        factors_i = nested_loop([],prime_factors,[],i)
        lower = i//3 + 1 #i/3 < lower
        if i%2 == 0:
            upper = i//2
        else:
            upper = i//2 + 1
        if lower < upper:
            all_frac += upper-lower
        else:
            continue
        
        for factor in factors_i:
            num = math.prod(factor)
            if len(factor)%2 == 1:
                pm = 1
            else:
                pm = -1
            num_low = lower//num
            if lower%num == 0:
                frac_n += pm
            f_range = upper - lower - 1 + lower%num
            if f_range < num:
                continue
            frac_n += pm*(f_range//num)
    return(all_frac-frac_n)

def pe_74(n):
    def get_digit_factorial(n):
        fact_sum = 0
        while n > 0:
            fact_sum += math.factorial(n%10)
            n = n//10
        return(fact_sum)
    term_60 = 0
    found = [1]*n
    digit_fact = {1:1,2:2,145:1,169:3,363601:3,1454:3,871:2,45361:2,872:2,45361:2,40585:1}

    for i in range(3,n):
        if found[i] == 0:
            continue
        chain = [i]
        curr = i
        while curr not in digit_fact:
            fact_sum = get_digit_factorial(curr)
            chain.append(fact_sum)
            curr = fact_sum
        inc = digit_fact[curr]
        m = len(chain)
        for j in range(m):
            chain_j = chain[j]
            val = m-1-j+inc
            if chain_j < n:
                found[chain_j] = 0
            if chain_j < n and val == 60:
                term_60 += 1
            digit_fact[chain_j] = val
    return(term_60)

def pe_75(L):
    def gen_pyth_prim(L):
        #generates all pythagorean primitive triples such that a+b+c <= L
        #returns list of tuples (a+b+c,a,b,c)
        #uses Euclid's formula https://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple
        n = int(np.sqrt(L)/2)+1
        prim = []
        for i in range(1,n):#i=n
            i_2 = i*i
            low = i+1
            #print((i,i_2,L))
            high = int((-i + np.sqrt(i_2+2*L))//2)+1
            for j in range(low,high,2):#j=m triples are primitive if i and j are coprime and exactly one is even
                if np.gcd(i,j) == 1:
                    j_2 = j*j
                    prim.append((2*j_2+2*j*i,j_2-i_2,2*i*j,i_2+j_2))
        return(prim)
    
    prim = gen_pyth_prim(L)

    pyth = np.zeros(L+1)
    for p in prim:
        length = p[0]
        ind = np.arange(1,L//length+1)*length
        pyth[ind] += 1
    single_tri_n = np.count_nonzero(pyth == 1)
    
    
    return(single_tri_n)

def pe_76(n):
    prev_part = [[0],[0,1,0],[0,0,0]]#element 0,i is only referenced for i = 0
    i = 2
    while True:
        for j in range(i,1,-1):
            i_j = 0
            for k in range(1,j+1):
                i_j += prev_part[i-k][min(i-k,k)]
            prev_part[i][j] = i_j
        prev_part[i][1] = 1
        
        if i > n:
            break
        i = i+1
        
        for j in range(1,i):
            prev_part[j].append(0)
        new_list = [0]*(i+1)
        prev_part.append(new_list)
    return(prev_part[i][i]-1)

def pe_77(n):
    primes = pehelperfunctions.gen_primes(10000)
    prev_part = [[0,0,1],[0,0,0],[0,0,0]] #prev_par[i][j] is how many sums of primes less or equal to primes[i] sum up to j
    i = 3
    while True:
        for j in range(len(prev_part)):
            prev_part[j].append(0)
        if primes[len(prev_part)] <= i:
            new_list = [0]*(i+1)
            prev_part.append(new_list)
        
        if i%2 == 0:
            prev_part[0][i] = 1
        for j in range(1,i+1):
            p_j = primes[j]
            if p_j >= i:
                if p_j == i:
                    prev_part[j][i] = prev_part[j-1][i] + 1
                break
            i_j = 0
            for k in range(j+1):
                p_k = primes[k]
                if i-p_k < primes[k] and i-p_k >=2:
                    l = k-1
                    p_l = primes[l]
                    while i-p_k < p_l:
                        l = l-1
                        p_l = primes[l]
                    
                    i_j += prev_part[l][i-p_k]
                else:
                    i_j += prev_part[k][i-p_k]
            prev_part[j][i] = i_j
        if prev_part[len(prev_part)-1][i] >= n:
            return(i)
        i = i+1

def pe_78(n):
    p_m = [1,1,2,3,5]
    m = 5
    while True:
        m_sum = 0
        i = 1
        while True:
            k = (i-1)//2 + 1
            if i%2 == 0:
                k = k*(-1)
            pent = k*(3*k-1)//2
            if pent > m:
                break
            if (k-1)%2 == 0:
                pm = 1
            else:
                pm = -1
            m_sum = m_sum + pm*p_m[m-pent]
            i += 1
        if m_sum%n == 0:
            return(m)
        p_m.append(m_sum)
        m = m+1

if __name__ == '__main__':
    completed = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,27,28,29,30,31,32,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,57,58,60,61
,62,63,64,65,66,67,69,71,72,73,74,75,76,77,78]
    inputs = {1:(3,5,1000),2:(4000000,),3:(600851475143,),4:(),5:(20,),6:(100,),7:(10001,),8:(PE_8_STRING,),9:(1000,),10:(2000000,),11:(PE_11_STRING,),12:(500,),
13:(PE_13_STRING,),14:(1000000,),15:(20,20),16:(1000,),17:(),18:(PE_18_STRING,),19:(),20:(100,),21:(10000,),22:(),23:(),24:(1000000,10),25:(1000,),27:(1000,1000),28:(1001,),
29:(100,),30:(),31:([1,2,5,10,20,50,100,200],200),32:(),34:(),35:(1000000,),36:(1000000,),37:(),38:(),39:(1000,),40:(),41:(),42:(),43:(),44:(),45:(),46:(),47:(),48:(1000,),
49:(),50:(1000000,),51:(),52:(),53:(),54:(),55:(),57:(),58:(),60:(),61:(),62:(),63:(),64:(),65:(100,),66:(1000,),67:(),69:(1000000,),71:(1000000,),72:(10**6,),
73:(12000,),74:(10**6,),75:(1500000,),76:(100,),77:(5000,),78:(10**6,)}
    total_time = 0
    highest_time = 0
    highest_problem = 0
    for i in completed:
        pe_func = "pe_" + str(i)
        args = inputs[i]
        exec(f"x = {pe_func}")

        start = timeit.default_timer()
        res = x(*args)
        end = timeit.default_timer()
        total_time = total_time + end-start
        if end-start > highest_time:
            highest_time = end-start
            highest_problem = i
        print("Problem: " + str(i))
        print("Result: " + str(res))
        print("Time: " + str(end-start))
    print("Total Time: " + str(total_time))
    print("Average Time: " + str(total_time/len(completed)))
    print("Longest Problem was Problem " + str(highest_problem) + " which took " + str(highest_time))