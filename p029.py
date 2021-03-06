# Project Euler - Problem 29
# -----------------------------------------------------------------------------
# Consider all integer combinations of a^b for 2 <= a <= 5 and 2 <= b <= 5:
#    4,   8,  16,   32
#    9,  27,  81,  243
#   16,  64, 256, 1024
#   25, 125, 625, 3125
# If they are then placed in numerical order, with any repeats removed, we get
# the following sequence of 15 distinct terms:
#   4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 625, 1024, 3125
# How many distict terms are in the sequence generated by a^b for 2 <= a <= 100
# and 2 <= b <= 100

import numpy as np
import time


def distPowers(nmin, nmax):
    a_min = nmin
    a_max = nmax
    b_min = nmin
    b_max = nmax
    powers = [[0 for i in range(a_max-a_min + 1)]
              for i in range(b_max-b_min + 1)]
    for i in range(len(powers)):
        for j in range(len(powers[0])):
            powers[i][j] = (i + a_min) ** (j + b_min)
    return np.unique(powers)


start = time.time()
p = distPowers(2, 100)
stop = time.time()
print(len(p))
print("Time: {} seconds".format(stop-start))
