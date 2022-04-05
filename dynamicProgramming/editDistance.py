# solving edit distance problem using dynamic programming

# edit distance between two strings is the minimum number of operations required to transform one string into the other.

"""
All operations are:
1. Add a character
2. Delete a character
3. Replace a character
"""

# The first input line has a string that contains n characters between A–Z.
stringN = str(input())
# The second input line has a string that contains m characters between A–Z.
stringM = str(input())

# Get the edit distance between the strings using dynamic programming
