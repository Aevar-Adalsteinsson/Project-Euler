import numpy as np
import timeit
import math
import itertools
import pehelperfunctions

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

if __name__ == '__main__':
    start = timeit.default_timer()
    res = pe_67()
    end = timeit.default_timer()
    print("Result: " + str(res))
    print("Time: " + str(end-start))