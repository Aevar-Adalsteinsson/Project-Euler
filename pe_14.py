import numpy as np
import timeit
import math
import itertools
import pehelperfunctions


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

if __name__ == '__main__':
    start = timeit.default_timer()
    res = pe_14(1000000)
    end = timeit.default_timer()
    print("Result: " + str(res))
    print("Time: " + str(end-start))