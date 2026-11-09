
def diamondPattern(n):
    k = (n + 1) // 2

    for i in range(1, k + 1):
        print(" " * (k-i) + "*" * (2*i-1))

    for i in range(k-1, 0, -1):
        print(" " * (k-i) + "*" * (2*i-1))


diamondPattern(5)
