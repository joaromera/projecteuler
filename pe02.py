# Project Euler problem #2 as in Hacker Rank
# https://www.hackerrank.com/contests/projecteuler/challenges/euler002

#!/bin/python3

import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    result = 0
    a = 1
    b = 1
    c = a + b
    while (c<n):
        result = result + c
        a = b + c
        b = c + a
        c = a + b
    print(result)
