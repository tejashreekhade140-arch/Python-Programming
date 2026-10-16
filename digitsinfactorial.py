import math

def digitsInFactorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    return len(str(math.factorial(n)))

print(digitsInFactorial(5))