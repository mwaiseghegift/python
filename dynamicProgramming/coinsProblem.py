# minimise coins problem using dynamic programming

def minCoins(coins, amount):
    """
    minimise coins problem using dynamic programming
    """
    # create a list of length amount+1
    # each element of the list will store the minimum number of coins required to make up that amount
    minCoins = [0] * (amount+1)
    # for each amount, find the minimum number of coins required to make up that amount
    for i in range(1, amount+1):
        # set the minimum number of coins to be the amount itself
        minCoins[i] = i
        # for each coin, check if the coin can be used to make up the amount
        for coin in coins:
            # if the coin can be used to make up the amount, check if the minimum number of coins required to make up the amount is less than the minimum number of coins required to make up the amount using the coin
            if coin <= i:
                minCoins[i] = min(minCoins[i], minCoins[i-coin]+1)
    return minCoins[amount]

#  input line with two integers n and x: the number of coins and the desired sum of money.
n, x = map(int, input().split())
# input line with n integers: the values of the coins.
coins = list(map(int, input().split()))


if minCoins(coins, x) > x:
    print(-1)
else:
    print(minCoins(coins, x))

# time complexity: O(N*6)