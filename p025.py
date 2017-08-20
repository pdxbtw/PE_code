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
start = time.time()

a = 0
b = 1
fib = a + b
index = 2
max_dig = 1000
while True:
    a = b
    b = fib
    fib = a + b
    index += 1
    fib_s = str(fib)
    if len(fib_s) == max_dig:
        break

stop = time.time()
print(index)
print('Processing Time: {} seconds'.format(stop-start))
