# tower of hanoi program using dynamic programming given n

def towerOfHanoi(n, source, destination, aux):
    if n == 1:
        print(source, " ", destination)
        return
    towerOfHanoi(n-1, source, aux, destination)
    print(  source, " ", destination)
    towerOfHanoi(n-1, aux, destination, source)

n = int(input(""))
# print an integer k: the minimum number of moves
k = 2**n - 1
print(k)
towerOfHanoi(n, "1", "2", "3")
