# count the number of ways to construct sum n by throwing a dice one or more times.
# Print the number of ways modulo 10^9+7.

def main():
    n = int(input("Enter n: "))
    dp = [0] * (n+1)
    dp[0] = 1
    for i in range(1, n+1):
        for j in range(1, 7):
            if i-j >= 0:
                dp[i] += dp[i-j]
        dp[i] %= 1000000007
    print(dp[n])

main()

