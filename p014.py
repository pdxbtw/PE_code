# Project Euler - Problem 14
# ----------------------------------------------------------------------------- 
# The following iterative sequence is defined for the set of positive integers:
#	n -> n/2 (n is even)
#	n -> 3n+1 (n is odd)
# Using the rule above and starting with 13, we generate the following
# sequence: 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
# It can be seen that this sequence (starting at 13 and finishing at) contains
# 10 terms. Although it has not been proved yet, it is thought that all
# starting numbers finish at 1. 
#
# Which starting number, under 1,000,000 produces the longest chain?

import time
import decimal
#getcontext().prec = 3
start = time.clock()

max_val = 0
max_num = 0
count = 0
temp = 0
num = 1
while num < 1000000:
    count = 0
    temp = num
    while temp != 1:
        count += 1
        if temp % 2 == 0:
            temp /= 2
        else:
            temp = temp * 3 + 1 
    # print(count)
    if count > max_val:
        max_num = num
        max_val = count
    num += 1
    if num % 10000 == 0:
        print(num)

end = time.clock()
print('\a')
print(max_val)
print(max_num)
print("Processing Time:", end - start, "seconds")
