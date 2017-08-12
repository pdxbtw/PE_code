#!/home/wilson_b/anaconda3/bin/python
# !/home/fure_j/Software/pypy3-2.4-linux_x86_64-portable/bin/pypy

# Project Euler - Problem 67
# -----------------------------------------------------------------------------
# By starting at the top of the triangle below (see problem 18) and moving to
# adjacent numbers on the row below, the maximum total from top to bottom is 23
# Find the maximum total from top to bottom in "triangle.txt", a 15K text file
# containing a triangle with one hundred rows.

from decimal import *
import time
import pdb
getcontext().prec = 3
start = time.clock()

tri = [0]*100
for i in range(100):
        tri[i] = [0]*(i+1)

with open("./files/p067_triangle.txt") as data:
        row = 0
        col = 0
        c = ''
        for line in data:
                for i in range(len(line)):
                        if line[i] == ' ':
                                tri[row][col] = int(c)
                                col += 1
                                c = ''
                        elif line[i] == '\n':
                                tri[row][col] = int(c)
                                col = 0
                                row += 1
                                c = ''
                        else:
                                c += line[i]
for r in range(len(tri)-1, 0, -1):
        for c in range(r):
                a = tri[r-1][c] + tri[r][c]
                b = tri[r-1][c] + tri[r][c+1]
                if a > b:
                        tri[r-1][c] = a
                else:
                        tri[r-1][c] = b
end = time.clock()
print(tri[0][0])
print("Processing Time:", Decimal(end) - Decimal(start), "seconds")
