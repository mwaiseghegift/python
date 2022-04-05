# tower of hanoi program using dynamic programming given n

def towerOfHanoi(n, source, destination, aux):
    if n == 1:
        print("Move disk 1 from rod", source, "to rod", destination)
        return
    towerOfHanoi(n-1, source, aux, destination)
    print("Move disk", n, "from rod", source, "to rod", destination)
    towerOfHanoi(n-1, aux, destination, source)

n = int(input("Enter number of disks: "))
towerOfHanoi(n, "A", "C", "B")
