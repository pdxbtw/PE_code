# Project Euler - Problem 14
# ----------------------------------------------------------------------------
# The following iterative sequence is defined for the set of positive
# integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following
# sequence:
#
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1)
# contains 10 terms. Although it has not been proved yet (Collatz Problem),
# it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
import time


def collatz(bound):
    colldict = {1: 0, 2: 1}
    while bound:
        if bound not in colldict:
            num = bound
            colltemp = []
            while num-1:
                if num in colldict:
                    a = len(colltemp) + colldict[num]
                    for ind, val in enumerate(colltemp):
                        colldict[val] = a - ind
                    break
                colltemp.append(num)
                if not num % 2:
                    num //= 2
                else:
                    num = num * 3 + 1
        bound -= 1
    max_num = max(colldict.values())
    max_key = [k for k, v in colldict.items() if v == max_num]
    return max_num, max_key[0]


start = time.time()
max_num, max_key = collatz(1000000)
stop = time.time()
print('The number {} has {} Collatz links'.format(max_key, max_num))
print("Time: {} seconds".format(stop-start))
