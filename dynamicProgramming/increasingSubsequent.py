# solve the increasing subsequence problem using dynamic programming

"""
You are given an array containing n integers. 
Your task is to determine the longest increasing subsequence in the array, i.e., 
the longest subsequence where every element is larger than the previous one.
A subsequence is a sequence that can be derived from the array by deleting some elements without 
changing the order of the remaining elements.
"""

# Function to return the length of the longest increasing subsequence
def increasingSubsequence(arr, n):
    # Create a table of size n and initialize all values as 1
    table = [1] * n

    # Compute optimized LIS values in bottom up manner
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and table[i] < table[j] + 1:
                table[i] = table[j] + 1

    # Return the maximum value from table
    return max(table)

n = int(input())
arr = list(map(int, input().split()))

print(increasingSubsequence(arr, n))