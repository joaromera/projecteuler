# Project Euler problem #5 as in Hacker Rank
# https://www.hackerrank.com/contests/projecteuler/challenges/euler005

#!/bin/python3

import sys
import math

def isPrime(x):
    if x != 2 and x % 2 == 0:
        return False
    for i in range(3,int(x**(1/2))+1,2):
        if x % i == 0:
            return False
    return True

t = int(input().strip())
listOfPrimes = []
for a0 in range(t):
    n = int(input().strip())
    smallest = 1
    exponent = 1
    for i in range(2,n+1):
        if ((i in listOfPrimes) or isPrime(i)) and i <= n:
            listOfPrimes = listOfPrimes + [i]
            exponent = int(math.log(n,i))
            smallest = smallest * (i**exponent)
        elif i > n:
            break
    print(smallest)
