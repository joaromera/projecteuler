# Project Euler problem #1 as in Hacker Rank
# https://www.hackerrank.com/contests/projecteuler/challenges/euler001

import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    n = n - 1
    divisibleBy3 = 3 * (((n//3) * ((n//3)+1)) // 2)
    divisibleBy5 = 5 * (((n//5) * ((n//5)+1)) // 2)
    divisibleBy15 = 15 * (((n//15) * ((n//15)+1)) // 2)
    result = divisibleBy3 + divisibleBy5 - divisibleBy15
    print(result)
