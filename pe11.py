# Project Euler problem #11 as in Hacker Rank
# https://www.hackerrank.com/contests/projecteuler/challenges/euler011

#!/bin/python3

import sys

grid = []
for grid_i in range(20):
   grid_t = [int(grid_temp) for grid_temp in input().strip().split(' ')]
   grid.append(grid_t)

#store temp result
result = 0

#checking rows
for _ in range(20):
    for i in range(17):
        if grid[_][i] * grid[_][i+1] * grid[_][i+2] * grid[_][i+3] > result:
            result = grid[_][i] * grid[_][i+1] * grid[_][i+2] * grid[_][i+3]

#checking columns
for i in range(20):
    for j in range(17):
        if grid[i][j] * grid[i][j+1] * grid[i][j+2] * grid[i][j+3] > result:
            result = grid[i][j] * grid[i][j+1] * grid[i][j+2] * grid[i][j+3]

#checking descending diagonals
for i in range(17):
    for j in range(17):
        if grid[i][j] * grid[i+1][j+1] * grid[i+2][j+2] * grid[i+3][j+3] > result:
            result = grid[i][j] * grid[i+1][j+1] * grid[i+2][j+2] * grid[i+3][j+3]

#checking ascending diagonals
for i in range(3,20):
    for j in range(17):
        if grid[i][j] * grid[i-1][j+1] * grid[i-2][j+2] * grid[i-3][j+3] > result:
            result = grid[i][j] * grid[i-1][j+1] * grid[i-2][j+2] * grid[i-3][j+3]

print(result)
