import numpy as np
import timeit
import math
import itertools
import pehelperfunctions

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



if __name__ == '__main__':
    start = timeit.default_timer()
    res = pe_42()
    end = timeit.default_timer()
    print("Result: " + str(res))
    print("Time: " + str(end-start))