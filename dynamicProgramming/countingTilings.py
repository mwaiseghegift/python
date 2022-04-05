
def countTilings(n, m):
    # create a 2D array of size n+1 x m+1
    dp = [[0 for i in range(m+1)] for j in range(n+1)]
    # base case
    for i in range(m+1):
        dp[0][i] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[n][m]

n, m = map(int, input().split())
print(countTilings(n, m) % 10**9+7)