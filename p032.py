#!/home/fure_j/Software/pypy3-2.4-linux_x86_64-portable/bin/pypy
# !/home/wilson_b/anaconda3/bin/python

# Project Euler - Problem 32
# -----------------------------------------------------------------------------
# We shall say than an n-digit number is pandigital if it makes use of all the
# digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1
# through 5 pandigital.
# The product 7254 is unusual, as the identity, 39x186=7254, containing 
# multiplicand, multiplier, and product is 1 through 9 pandigital.
# Find the sum of all products whose multiplicand/multiplier/product identity
# can be written as a 1 through 9 pandigital.
# HINT: Some products can be obtained in more than one way so be sure to only 
# include it on ce in your sum.

from decimal import *
import time
import pdb
getcontext().prec = 3
#pdb.set_trace()
start = time.clock()

a = 1
b = 0
dig_num = 0
digits = ('1', '2', '3', '4', '5', '6', '7', '8', '9')
num_l = []
while a < 100:
        a += 1
        b = 10000//a
        while a < b:
                p = a * b
                s = str(a) + str(b) + str(p)
                len_s = len(s)
                if len_s == 9:
                        pan_dig = True
                        for i in digits:
                                if i not in s:
                                        pan_dig = False
                                        break
                        if pan_dig:
                                num_l += [p]
                b -= 1
num_l = set(num_l)
end = time.clock()
print(sum(num_l))
print("Processing time:", Decimal(end) - Decimal(start), "seconds")


