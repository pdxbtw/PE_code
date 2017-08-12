#!/home/fure_j/Software/pypy3-2.4-linux_x86_64-portable/bin/pypy
# !/home/wilson_b/anaconda3/bin/python

# Project Euler - Problem 40
# -----------------------------------------------------------------------------
# An irrational decimal fraction is created by concatenating the positive 
# integers: 0.1234567891011121314...
# It can be seen that the 12th digit of the fractional part is 1.
# if dn represents the nth digit fractional part, find the value of the 
# following expression.
#   d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000

from decimal import *
import time
import pdb
getcontext().prec = 3
start = time.clock()

dig_count = 0
num = 0
dig_list = []
order = 1
while dig_count < 1000000:
        num += 1
        if num < 10:
                dig_count += 1
                if dig_count >= order:
                        index = -1*(1 + dig_count - order)
                        temp = str(num)
                        dig_list.append(temp[index])
                        order *= 10
                continue
        elif num < 100:
                dig_count += 2
                if dig_count >= order:
                        index = -1*(1 + dig_count - order)
                        temp = str(num)
                        dig_list.append(temp[index])
                        order *= 10
                continue
        elif num < 1000:
                dig_count += 3
                if dig_count >= order:
                        index = -1*(1 + dig_count - order)
                        temp = str(num)
                        dig_list.append(temp[index])
                        order *= 10         
                continue
        elif num < 10000:
                dig_count += 4
                if dig_count >= order:
                        index = -1*(1 + dig_count - order)
                        temp = str(num)
                        dig_list.append(temp[index])
                        order *= 10
                continue
        elif num < 100000:
                dig_count += 5
                if dig_count >= order:
                        index = -1*(1 + dig_count - order)
                        temp = str(num)
                        dig_list.append(temp[index])
                        order *= 10
                continue
        else:
                dig_count += 6
                if dig_count >= order:
                        index = -1*(1 + dig_count - order)
                        temp = str(num)
                        dig_list.append(temp[index])
                        order *= 10
                continue
        num += 1

print(dig_list)
prod = 1
for i in dig_list:
        prod *= int(i)

end = time.clock()
print(prod)
print("Processing time:", Decimal(end) - Decimal(start), "seconds")

