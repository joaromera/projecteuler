# Project Euler problem #3 as in Hacker Rank
# https://www.hackerrank.com/contests/projecteuler/challenges/euler003

#!/bin/python3

import sys

def isPrime(x):
    if x != 2 and x % 2 == 0:
        return False
    for i in range(3,int(x**(1/2))+1,2):
        if x % i == 0:
            return False
    return True

t = int(input().strip())

for a0 in range(t):
    n = int(input().strip())
    if n % 2 == 0:
        bigFactor = 2
        n = n // 2
        while n % 2 == 0:
            n = n // 2
    else:
        bigFactor = 1

    factor = 3
    limit = n**(1/2)
    while n > 1 and factor <= limit:
        if n % factor == 0:
            n = n // factor
            bigFactor = factor
            while n % factor == 0:
                n = n // factor
            limit = n**(1/2)
        factor = factor + 2
    if n == 1:
        print(bigFactor)
    else:
        print(n)
