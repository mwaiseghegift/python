# calculate the number of distinct ways you can produce sum x using the available coins

# first input line has two integers n and x: the number of coins and the desired sum of money.
n, x = map(int, input().split())

# second line has n distinct integers: the values of the coins.
coins = list(map(int, input().split()))

# function to calculate the number of distinct unordered subsets of a set of n elements
def coinCombination(coins, x):
    # create a list of zeros of length x+1
    # the first element is 0, the last element is x
    # the rest of the elements are initialized to 0
    ways = [0] * (x+1)
    ways[0] = 1
    for i in range(len(coins)):
        for j in range(coins[i], x+1):
            ways[j] += ways[j-coins[i]]
    return ways[x]

print(coinCombination(coins, x))

