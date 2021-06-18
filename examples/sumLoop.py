""" Write a python program to calculate the sum of 
numbers to the one given in the input """


num = int(input("Enter the number: "))
sum=0
while(num>0):
    sum = sum+num
    num = num-1

print(sum)