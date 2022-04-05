
def elevatorRides(n, weight, maxWeight):
    # create a 2D array of size n+1 x maxWeight+1
    dp = [[0 for i in range(maxWeight+1)] for j in range(n+1)]
    # base case
    for i in range(maxWeight+1):
        dp[0][i] = 0
    # fill the dp array
    for i in range(1, n+1):
        for j in range(maxWeight+1):
            if j >= weight[i-1]:
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-weight[i-1]]+1)
            else:
                dp[i][j] = dp[i-1][j]
    # return the last element of the last row
    return dp[n][maxWeight]

n, maxWeight = map(int, input().split())
weight = list(map(int, input().split()))
print(elevatorRides(n, weight, maxWeight))



