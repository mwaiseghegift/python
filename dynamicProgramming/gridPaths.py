# Consider an n×n grid whose squares may have traps. 

# func to calculate the number of paths from the upper-left square to the lower-right square. You can only move right or down.
# It is not allowed to move to a square with a trap.

def gridPaths(n):
    # create a 2D array of size n x n
    grid = [[0 for x in range(n)] for y in range(n)]
    # set the first row and column to 1
    grid[0][0] = 1
    # loop through the grid
    for i in range(n):
        for j in range(n):
            # if the current square is not a trap, set the value to the sum of the values of the squares above and to the left
            if grid[i][j] != -1:
                if i > 0:
                    grid[i][j] += grid[i-1][j]
                if j > 0:
                    grid[i][j] += grid[i][j-1]
            # if the current square is a trap, set the value to -1
            else:
                grid[i][j] = -1
    # return the value of the lower-right square
    return grid[n-1][n-1]
   

# input line has an integer n: the size of the grid.
n = int(input())
# n  lines that describe the grid. Each line has n characters: . denotes an empty cell, and * denotes a trap.
for i in range(n):
    grid = input()
    # print the number of paths from the upper-left square to the lower-right square
   
# Print the number of paths modulo 10^9+7
print(gridPaths(n) % (10**9 + 7))