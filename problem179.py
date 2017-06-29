# Problem 179... timing out, work in progress.
# https://www.hackerrank.com/contests/projecteuler/challenges/euler179/problem

def multiples(n, divisors):
    multlist = []
    to = (n // 2) + 1
    for i in range(1, to):
        if i in divisors.keys() and n % i == 0:
            multlist += divisors[i]
        else:
            if (n % i == 0):
                multlist += [i]
    multlist += [n]
    return list(set(multlist))

multdict = {1: [1]}

t = int(input())

for i in range(t):
    n = int(input())
    total = 0
    for i in range(2, n + 1):
        if i not in multdict.keys():
            multdict[i] = multiples(i, multdict)
        if len(multdict[i]) == len(multdict[i - 1]):
            total += 1
    print(total)
