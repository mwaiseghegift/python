# Edit distance Problem
"""
Computes the edit distance between two strings.
"""

def editDistance(string1, string2):
    m = len(string1)
    n = len(string2)
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(m+1):
        dp[i][0] = i
    for j in range(n+1):
        dp[0][j] = j
    for i in range(1, m+1):
        for j in range(1, n+1):
            if string1[i-1] == string2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
    return dp[m][n]

n = input()
m = input()
print(editDistance(n, m))