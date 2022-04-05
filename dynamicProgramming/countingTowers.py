# solving the countingTowers problem using dynamic programming approach

t = int(input())
array = []
for i in range(t):
    array.append(int(input()))

def countTowers(array, n):
    dp = [[0 for i in range(n+1)] for j in range(n+1)]
    for i in range(1, n+1):
        dp[i][i] = 1
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[n][n]

print(countTowers(array, t) % 10**9+7)
