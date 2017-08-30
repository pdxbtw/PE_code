# Project Euler - Problem 24
# -----------------------------------------------------------------------------
# A permutation is an ordered arrangement of objects. For example, 3124 is one
# possible permutation of the digits 1, 2, 3 and 4. If all of the permutations
# are listed numerically, we call it lexicographic order. The lexicographic
# permutations of 0, 1 and 2 are:
#   012 021 102 120 201 210
# What is the millionth lexicographic permutation of the 0,1,2,3,4,5,6,7,8,9 ?

import time
import math
start = time.time()

num_dig = 10
word = [i for i in range(num_dig)]
order_num = 1e6
order_num -= 1
fact = [math.factorial(i+1) for i in range(num_dig)]
temp = [0, ]
if order_num > fact[-1]:
    print('The index selected is too high!')
else:
    count = 0
    for i in range(len(fact)-1, 0, -1):
        shift = int(order_num // fact[i-1])
        temp = word.pop(count + shift)
        word.insert(count, temp)
        order_num %= fact[i-1]
        count += 1

end = time.time()
print(word)
print('Time: {} seconds'.format(end-start))
