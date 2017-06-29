# Project Euler problem #37 as in Hacker Rank
# https://www.hackerrank.com/contests/projecteuler/challenges/euler037

import sys
from math import sqrt; from itertools import count, islice

def is_prime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

def isTruncatablePrime(n):
    stringed = str(n)
    stringedrev = stringed[::-1]
    length = len(stringed)
    for num in range(length):
        if not is_prime(int(stringed[0:num+1])) or not is_prime(int(stringed[length-num-1:])):
            return False
    return True

def sumTruncatableUnder100(n):
    firstDig = [2,3,5,7]
    lastDig = [3,7]
    total = 0
    for i in firstDig:
        for j in lastDig:
            check = int(str(i) + str(j))
            if isTruncatablePrime(check):
                total += int(check)
    return total

def bigTruncatableSum(n):
    firstDig = [2,3,5,7]
    lastDig = [3,7]
    total = 186
    checking = 0
    modulo = 10
    rango = 10
    start = 1
    while int(checking) < n:
        for i in firstDig:
            for j in range(start,modulo,2):
                veamo = j % modulo
                for k in lastDig:
                    if i == 7 and k == 7 and j == (modulo - 1):
                        modulo = modulo * 10
                        start = modulo //10 + 1
                    checking = str(i) + str(veamo) + str(k)
                    if int(checking) > n:
                        return total
                    criterioTres = 0
                    for char in checking:
                        criterioTres += int(char)
                    if criterioTres % 3 == 0:
                        continue
                    if not isTruncatablePrime(int(checking)):
                        continue
                    total += int(checking)


    return ("this is " + str(total))

n = int(input())

if n <= 100:
    print(sumTruncatableUnder100(n))
else:
    print(bigTruncatableSum(n))
