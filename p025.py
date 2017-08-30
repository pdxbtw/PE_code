# Project Euler - Problem 25
# -----------------------------------------------------------------------------
# The Fibonacci sequence is defined by the recurence relation:
# Fn = Fn-1 + Fn-2, where F1 = 1 and F = 1
# Hence, the first 12 terms will be:
#   1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
# The 12th term is ther first term to contain 3 digits.
# What is the index of the first term in the Fibonacci sequence to contain
# 1000 digits?

import time


def fibonacciOrder(order):
    a, b = 0, 1
    index = 1
    while True:
        a, b = b, a + b
        index += 1
        if len(str(b)) == order:
            break
    return index


start = time.time()
n_dig = 1000
index = fibonacciOrder(n_dig)
stop = time.time()
print(index)
print('Time: {} seconds'.format(stop-start))
