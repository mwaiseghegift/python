
def getCount(a,b):
    # create a list of all the numbers between a and b
    nums = [i for i in range(a,b+1)]
    # create a list of all the numbers between a and b with no two adjacent digits being the same
    nums2 = [i for i in nums if i%10 != i//10%10]
    # return the length of the list
    return len(nums2)

a,b = map(int,input().split())
print(getCount(a,b))