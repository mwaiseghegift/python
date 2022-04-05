
def rectangleCutting(a, b):
    # dp array to store the minimum number of moves to cut it into two rectangles in such a way that all side lengths remain integers
    dp = [[0 for i in range(b+1)] for j in range(a+1)]

    # base case
    for i in range(1, a+1):
        dp[i][1] = 1

    for i in range(1, b+1):
        dp[1][i] = 1

    # fill the dp array
    for i in range(2, a+1):
        for j in range(2, b+1):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1

    return dp[a][b]

# input line has two integers a and b.
a , b = map(int, input().split())

print(rectangleCutting(a, b))