# Project Euler problem #8 as in Hacker Rank
# https://www.hackerrank.com/contests/projecteuler/challenges/euler008

#!/bin/python3

import sys

t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = input().strip()
    tempNum = 0
    for i in range(len(num)-k+1):
        InnerProd = 1
        for j in num[i:i+k]:
            InnerProd = InnerProd * int(j)
        if InnerProd > tempNum:
            tempNum = InnerProd
    print(tempNum)
