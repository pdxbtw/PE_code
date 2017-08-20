# Project Euler - Problem 21
# -----------------------------------------------------------------------------
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n
# which divide evenly into n). If d(a) = b and d(b) = a, where a!=b, then a and
# b are an amicable pair and each of a and b are called amicable numbers.
# Evaluate the sum of all the amicable numbers under 10,000

import time
start = time.clock()

num = 0
tot = 0
while num < 1e4:
    num = 1e4
end = time.clock()
print('Processing Time: {} seconds'.format(end-start))
