# Project Euler problem #6 as in Hacker Rank
# https://www.hackerrank.com/contests/projecteuler/challenges/euler006

#!/bin/python3

import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    sumOfSquares = (n * (n+1) * (2*n + 1)) // 6
    squareOfSum = ((n*(n+1))//2)*((n*(n+1))//2)
    print(squareOfSum - sumOfSquares)
