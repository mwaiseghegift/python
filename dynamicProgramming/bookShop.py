# The number of books and the maximum total price.
n, x = map(int, input().split())
# the prices of the books.
h = list(map(int, input().split()))
# number of pages of the books
pages = list(map(int, input().split()))


def maxPages(pages, h, x):
    # create a list to store the maximum number of pages you can buy
    maxPages = [0] * (x + 1)
    # loop through the list
    for i in range(len(h)):
        # loop through the list
        for j in range(x, h[i] - 1, -1):
            # if the current price is less than the current max price, update the max price
            if h[i] <= j:
                maxPages[j] = max(maxPages[j], maxPages[j - h[i]] + pages[i])
    # return the max price
    return maxPages[x]

print(maxPages(pages, h, x))