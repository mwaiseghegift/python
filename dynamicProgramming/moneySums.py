def moneySums(arr, n):
    """
    :param arr: array of integers
    :param n: number of elements in arr
    :return: number of ways to sum money
    """
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
    for i in range(n-1):
        dp[i][i+1] = 1 if arr[i] == arr[i+1] else 0
    for i in range(2, n):
        for j in range(i, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[n-1][n-1]

n = int(input())
arr = list(map(int, input().split()))
print(moneySums(arr, n))

#  print all possible sums in increasing order.
for i in range(n):
    for j in range(i, n):
        print(arr[i:j+1], sum(arr[i:j+1]))


