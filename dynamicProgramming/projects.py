
# Function to return the maximum amount of money you can earn
def maxMoney(arr, n):
    # Create a table of size n and initialize all values as 0
    table = [0] * n

    # Compute optimized LIS values in bottom up manner
    for i in range(1, n):
        for j in range(0, i):
            if arr[i][0] > arr[j][0] and arr[i][1] < arr[j][1] and table[i] < table[j] + arr[i][2]:
                table[i] = table[j] + arr[i][2]

    # Return the maximum value from table
    return max(table)

n = int(input())

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))


print(maxMoney(arr, n))
