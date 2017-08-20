# Project Euler - Problem 15
# -----------------------------------------------------------------------------
# Starting from the top left corner of a 2x2 grid, and only being able to move
# to the right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20x20 grid?

import math
import time
start = time.time()

ans = math.factorial(40)/(math.factorial(20) * math.factorial(20))

end = time.time()
print(ans)
print('Processing Time: {} seconds'.format(end-start))
