# Project Euler - Problem 42
# -----------------------------------------------------------------------------
# The nth term of the sequence of triangle numbers if given by, tn=1/2(n(n+1));
# so the first ten triangle numbers are:
#       1,3,6,10,15,21,28,36,45,55,...
# By converting each letter in a word to a number corresponding to its alpha-
# betical position and adding these values we from a word value. For example,
# the word value for SKY is 19+11+25+=55+t10. If the word value is a triangle
# number then we shall call the word a triangle word.
# Using words.txt, a 16K text file containing nearly two-thousand common
# English words, how many are triangle words?

import time
import csv
import urllib.request

start = time.time()
url = 'https://projecteuler.net/project/resources/p042_words.txt'
filename, header = urllib.request.urlretrieve(url, 'words.txt')
with open(filename) as f:
        readCSV = csv.reader(f, delimiter=',')
        words = []
        for row in readCSV:
                words = row
max_len = 0
for i in words:
        temp = len(i)
        if temp > max_len:
                max_len = temp

max_num = 26*max_len
tri = []
n = 0
while True:
        n += 1
        tri_num = int(n*(n+1)/2)
        if tri_num > max_num:
                break
        else:
                tri.append(tri_num)

count = 0
for i in words:
        temp = 0
        for j in i:
                temp += ord(j)-64
        if temp in tri:
                count += 1

stop = time.time()
print(count)
print("Time: {} seconds".format(stop-start))
