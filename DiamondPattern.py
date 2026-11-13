
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

#Right Triangle Pattern

def rightTrianglePattern(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print("*", end="")
        print()


rightTrianglePattern(3)

#invertTriangle 

def invertedTriangle(n):
    for i in range(n, 0, -1):
        for j in range(i):
            print("*", end="")
        print()


invertedTriangle(5)

#Centered Pyramid Pattern

def centeredPyramidPattern(n):
    for i in range(1, n + 1):
        spaces = " " * (n - i)
        stars = "*" * (2 * i - 1)

        print(spaces + stars)


centeredPyramidPattern(4)

#Floyd's Triangle Pattern

def floydsTriangle(n):
    num = 1

    for i in range(1, n + 1):
        for j in range(i):
            print(num, end=" ")
            num += 1

        print()


floydsTriangle(4)

#Find Duplicate Number

def findDuplicate(numbers):
    seen = set()

    for num in numbers:
        if num in seen:
            return num

        seen.add(num)

    return -1


numbers = [1, 3, 4, 2, 2]

print("Duplicate Number:", findDuplicate(numbers))

#Hollow Pyramid Pattern

def hollowPyramidPattern(n):
    for i in range(1, n + 1):

        if i == 1:
            print(" " * (n-1) + "*")

        elif i == n:
            print("*" * (2*n-1))

        else:
            print(" " * (n-i) + "*" + " " * (2*i-2) + "*")

hollowPyramidPattern(4)

#Butterfly Pattern

def butterflyPattern(n):
    # Upper half
    for i in range(1, n + 1):
        print("*" * i + " " * (2 * (n-i)) + "*" * i)

    # Lower half
    for i in range(n-1, 0, -1):
        print("*" * i + " " * (2 * (n-i)) + "*" * i)


butterflyPattern(4)

#armstrong number in range

def armstrongInRange(start, end):
    for num in range(start, end + 1):
        original = num
        length = len(str(num))
        total = 0

        while num > 0:
            digit = num % 10
            total += digit ** length
            num //= 10

        if total == original:
            print(original)


armstrongInRange(100, 200)

