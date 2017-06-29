# Project Euler problem #7 as in Hacker Rank
# https://www.hackerrank.com/contests/projecteuler/challenges/euler007

#!/bin/python3

import sys
from math import sqrt; from itertools import count, islice

def is_prime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

lista = [2]
populateList = 3

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    while len(lista) <= n:
        # print(populateList, lista)
        if is_prime(populateList):
            lista = lista + [populateList]
        populateList = populateList + 2
    if len(lista) >= n or n == 1:
        print(lista[n-1])
