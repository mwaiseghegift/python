
# function to find all money sums you can create using these coins
def moneySums(coins, money):
    # create a list of lists to store the results
    results = [[0 for x in range(money + 1)] for x in range(len(coins) + 1)]

    # fill the first row and column with 1
    for i in range(len(coins) + 1):
        results[i][0] = 1

    # fill the rest of the table
    for i in range(1, len(coins) + 1):
        for j in range(1, money + 1):
            if j >= coins[i - 1]:
                results[i][j] = results[i - 1][j] + results[i][j - coins[i - 1]]
            else:
                results[i][j] = results[i - 1][j]

    # print the results
    print("\nResults:")
    for i in range(len(coins) + 1):
        print(results[i])


    # return the results
    return results[len(coins)][money]

# input line has an integer n: the number of coins.
n = int(input())

# n  integers x1,x2,…,xn: the values of the coins.
coins = list(map(int, input().split()))

print(moneySums(coins, n))

