import numpy as np
import timeit
import math
import itertools
import pehelperfunctions




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
            



if __name__ == '__main__':
    pyramid = '''75
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
    start = timeit.default_timer()
    res = pe_18(arg)
    end = timeit.default_timer()
    print("Result: " + str(res))
    print("Time: " + str(end-start))