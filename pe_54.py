import numpy as np
import timeit
import math
import itertools
import pehelperfunctions



if __name__ == '__main__':
    start = timeit.default_timer()
    res = pe_54()
    end = timeit.default_timer()
    print("Result: " + str(res))
    print("Time: " + str(end-start))