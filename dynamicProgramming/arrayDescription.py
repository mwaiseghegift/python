
#n and m: the array size and the upper bound for each value.
n, m = map(int, input().split())
#The second input line has n integers.
x = list(map(int, input().split()))

def countArrays(x, m):
    # create a list to store the maximum number of pages you can buy
    maxPages = [0] * (m + 1)
    # loop through the list
    for i in range(len(x)):
        # loop through the list
        for j in range(m, x[i] - 1, -1):
            # if the current price is less than the current max price, update the max price
            if x[i] <= j:
                maxPages[j] = max(maxPages[j], maxPages[j - x[i]] + 1)
    # return the max price
    return maxPages[m]

# The number of arrays modulo 10^9+7
print(countArrays(x, m) % (10**9 + 7))

