#!/home/fure_j/Software/pypy3-2.4-linux_x86_64-portable/bin/pypy
# !/home/wilson_b/anaconda3/bin/python

# Project Euler - Problem 35
# -----------------------------------------------------------------------------
# The number, 197, is called a circular prime because all rotations of the 
# digits: 197, 971, and 719, are themselves prime. There are 13 such primes
# below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97. How many 
# circular primes are there below one million?

from decimal import *
import math
import time
import pdb
getcontext().prec = 3
#pdb.set_trace()
start = time.clock()

count = 13
primes = (2,)
circ_prime = []
test_val = 3
prime = True
run = True
while run:
        stop = math.floor(math.sqrt(test_val))
        prime = True
        for i in primes:
                if i > stop:
                        break
                if test_val % i == 0:
                        prime = False
                        break
        if prime:
                primes += (test_val, )
        test_val += 2
        if test_val > 1000000:
                run = False
for i in primes:
        circ = True
        num_s = str(i)
        for j in range(len(num_s)-1):
                num_s = num_s[1:] + num_s[0]
                if int(num_s) not in primes:
                        circ = False
                        break
        if circ:
                circ_prime += [i]
end = time.clock()
print(len(circ_prime))
print("Processing Time:", Decimal(end) - Decimal(start), "seconds")
