
number = int(input("Enter the number to recurse"))

def recursiceNumber(n):
    if (n==1):
        print(1)
    else:
        print(n*recursiceNumber(n-1))