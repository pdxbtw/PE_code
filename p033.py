# Project Euler - Problem 33
# -----------------------------------------------------------------------------
# The fraction 49/98 is a curious fraction, as an inexperienced mathematician
# in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which
# is correct, is obtained by cancelling the 9s.
# We shall consider fractions like, 30/50=3/5, to be trivial examples.
# There are exactly four non-trivial examples of this type of fraction, less
# than one in value, and containing two digits in the numerator and
# denominator.
# If the product of these four fractions is given in its lowest commmon term,
# find the value of the denominator.

import time


def findOddFractions():
    num_l = []
    den_l = []
    nums = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
    for num in range(11, 99):
        for den in range(11, 99):
            for i in nums:
                num_s = str(num)
                den_s = str(den)
                if (i in num_s) and (i in den_s):
                    j = den_s.index(i)
                    if j:
                        den_n = int(den_s[0])
                    else:
                        den_n = int(den_s[1])

                    k = num_s.index(i)
                    if k:
                        num_n = int(num_s[0])
                    else:
                        num_n = int(num_s[1])
                    if den_n != 0:
                        val_1 = num/den
                        val_2 = num_n/den_n
                        if (val_1 == val_2) and (val_1 < 1):
                            # message = "Value 1 = {}/{}\tValue 2 = {}/{}"
                            # print(message.format(num, den, num_n, den_n))
                            den_l += [den_n]
                            num_l += [num_n]
    prod_n = 1
    prod_d = 1
    for ind, _ in enumerate(den_l):
        prod_n *= num_l[ind]
        prod_d *= den_l[ind]
    i = 2

    # Simplify fraction
    while i <= prod_n:
        if (prod_n % i == 0) and (prod_d % i == 0):
            prod_n /= i
            prod_d /= i
        else:
            i += 1
    return prod_d


start = time.time()
prod_d = findOddFractions()
stop = time.time()
print("{}".format(prod_d))
print("Time: {} seconds".format(stop-start))
