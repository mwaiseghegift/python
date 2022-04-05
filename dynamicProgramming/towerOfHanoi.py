
def towerOfHanoi(n, source, destination, aux):
    if n == 1:
        print(source, " ", destination)
        return
    towerOfHanoi(n-1, source, aux, destination)
    print(  source, " ", destination)
    towerOfHanoi(n-1, aux, destination, source)

n = int(input(""))

k = 2**n - 1
print(k)
towerOfHanoi(n, "1", "2", "3")
