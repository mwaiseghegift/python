
number = int(input("Enter the number: "))

def recursiceNumber(n):
    if (n==1):
        return 1
    else:
        return n*recursiceNumber(n-1)
        

print(recursiceNumber(number))