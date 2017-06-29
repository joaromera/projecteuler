# Project Euler problem #15 as in Hacker Rank
# https://www.hackerrank.com/contests/projecteuler/challenges/euler015

import sys
import math

t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    size = n+k
    result = (math.factorial(size)//(math.factorial(n)*math.factorial(k))) % ((10**9)+7)
    print(result)
