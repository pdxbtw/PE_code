# Project Euler - Problem 2
# Each new term in the Fibonacci sequence is generated by adding the
# previous two terms. By starting with 1 and 2, the first 10 terms will be:
#    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not
# exceed four million, find the sum of the even-valued terms.

import time


# Starting with 1,1,2,3,5,8,13,21,34... we can see that every third value
# in the sequence is even and we can skip the conditional statements
def evenFibonaciSum(top_limit):
    total = 0
    a, b = 0, 1
    while a < top_limit:
        total += a
        a, b = b, a+b
        a, b = b, a+b
        a, b = b, a+b
    return total


start = time.time()
total = evenFibonaciSum(4e6)
stop = time.time()
print(total)
print('Time: {} seconds'.format(stop - start))
