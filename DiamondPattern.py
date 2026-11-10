
def diamondPattern(n):
    k = (n + 1) // 2

    for i in range(1, k + 1):
        print(" " * (k-i) + "*" * (2*i-1))

    for i in range(k-1, 0, -1):
        print(" " * (k-i) + "*" * (2*i-1))


diamondPattern(5)

#Pattern Printing

def numberTrianglePattern(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


numberTrianglePattern(3)

#Multiplication Table

def multiplicationTable(n, limit):
    for i in range(1, limit + 1):
        print(n * i)


multiplicationTable(3, 5)

