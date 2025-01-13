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