# Project Euler - Problem 26
# -----------------------------------------------------------------------------
# A unit fraction contains 1 in the numerator. The decimal representation of
# the unit fractions with denominators 2 to 10 are given:

#      1/2    =   0.5
#      1/3    =   0.(3)
#      1/4    =   0.25
#      1/5    =   0.2
#      1/6    =   0.1(6)
#      1/7    =   0.(142857)
#      1/8    =   0.125
#      1/9    =   0.(1)
#      1/10   =   0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It
# can be seen that 1/7 has a 6-digit recurring cycle.

# Find the value of d < 1000 for which 1/d contains the longest recurring
# cycle in its decimal fraction part.

import time


def longRepeatDec(bound):
    n = [i for i in range(3, bound+1)]
    # Remove non repeating values
    for i in range(5):
        for j in range(10):
            k = (5**i) * (2**j)
            if k in n:
                n.remove(k)
            else:
                break
    print(len(n))
    return 0


start = time.time()
ans = longRepeatDec(1000)
stop = time.time()
print(ans)
print("Time: {} seconds".format(stop-start))
