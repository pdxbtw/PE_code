# Project Euler - Problem 1
# If we list all the natrual numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6, and 9. The sum of these multiples is 23. Find the sum of all
# the multiples of 3 or 5 below 1000.

import time
import decimal
getcontext().prec = 3
start = time.clock()

total = 0
count = 1
while count < 1000:
    if count % 3 == 0:
        total += count
    elif count % 5 == 0:
        total += count
    count += 1	
end = time.clock()
print(total)
print('Processing Time:',  Decimal(end) - Decimal(start), 'seconds')
