# Project Euler - Problem 98
# -----------------------------------------------------------------------------
# By replacing each of the letters in the word CARE with 1,2,9, and 6
# respectively, we form a square number: 1296 = 36^2. What is remarkable is
# that, by using the same digital substitution, the anagram, RACE, also forms a
# square number: 9216 = 96^2. We shall call CARE (and RACE) a square anagram
# word pair and specify further that leading zeroes are not permitted, neither
# may a different letter have the same digital value as another letter.
# Using the provided text file, find all the square anagram word pairs (a
# palindromic word is NOT considered to be an anagram of itself).
# What is the largest square number fromed by any member of such a pair?

import time
import csv
import math
import urllib.request

# import pdb
start = time.time()

url = 'https://projecteuler.net/project/resources/p098_words.txt'
filename, header = urllib.request.urlretrieve(url, 'words.txt')
with open(filename) as f:
        data = csv.reader(f, delimiter=',')
        w = []
        for row in data:
                w = row

words = []
for i in range(1, 15):
    temp = []
    for j in w:
        if len(j) == i:
            temp.append(j)
    words.append(temp)

for i in range(2, len(words)):
    l = len(words[i])
    n = 0
    while n < l:
        s = sorted(words[i][n])
        d = 1
        for j in range(l):
            if j != n:
                temp = sorted(words[i][j])
                if temp == s:
                    d = 0
                    break
        if d:
            del words[i][n]
            l -= 1
        else:
            print(words[i][n])
            n += 1

sqrs = []
for i in range(len(words)):
    temp = []
    if len(words[i]) != 0:
        low = math.floor(math.sqrt(10**i))
        high = math.ceil(math.sqrt(10**(i+1)))
        for j in range(low, high):
            temp.append(j**2)

        if (i == 8) or (i == 7):
            l = len(temp)
            n = 0
            while n < l:
                if len(set(str(temp[n]))) != (i+1):
                    temp.remove(temp[n])
                    l -= 1
                else:
                    n += 1

        l = len(temp)
        n = 0
        while n < l:
            s = sorted(str(temp[n]))
            d = 1
            for k in range(l):
                if k != n:
                    temp_s = sorted(str(temp[k]))
                    if temp_s == s:
                        d = 0
                        break
            if d:
                del temp[n]
                l -= 1
            else:
                n += 1
        sqrs.append(temp)
    else:
            sqrs.append([])

print("hello")
for i in range(len(sqrs)):
    print(len(sqrs[i]))

stop = time.time()
print(max(sqrs))
print("Time: {} seconds".format(stop-start))
