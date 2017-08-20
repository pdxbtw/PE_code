# Project Euler - Problem 16
# -----------------------------------------------------------------------------
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26
# What is the sum of the digits of the number 2^1000?

import time
start = time.time()

n = 2**1000
s = str(n)
length = len(s)
total = 0
for n in range(length):
    total += int(s[n])

stop = time.time()
print(total)
print('Time: {} seconds'.format(stop-start))
