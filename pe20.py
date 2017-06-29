# Project Euler problem #20 as in Hacker Rank
# https://www.hackerrank.com/contests/projecteuler/challenges/euler020

import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    factorial = 1
    result = 0
    for i in range(1,n+1):
        factorial *= i
    for i in str(factorial):
        result += int(i)
    print(result)
