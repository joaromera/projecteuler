# Project Euler problem #4 as in Hacker Rank
# https://www.hackerrank.com/contests/projecteuler/challenges/euler004

#!/bin/python3

import sys

def isPalindrome(n):
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    palindrome = 0
    for i in range (999,99,-1):
        for j in range(999,i-1,-1):
            if (i*j) < palindrome:
                break
            if (i*j) < n and isPalindrome(i*j) and (i * j) > palindrome:
                palindrome = (i*j)
                break
    print(palindrome)
