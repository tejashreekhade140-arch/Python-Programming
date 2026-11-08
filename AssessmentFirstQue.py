#1. Generate a sequence of odd numbers
def sequence(n):
    seq = []

    for i in range(n, 0, -2):
        if i % 2 != 0:
            seq.append(i)

    return seq


print(sequence(11))

#2.Generate number excluding multiples of 7
def number(n):
    total=[]
    for i in range (n,51):
        if i % 7 == 0:
            continue
        else:
            total.append(i)
    return total
print(number(11))

#3. Find largest digit in a number

def largest(n):
    largest_digit = 0

    while n > 0:
        digit = n % 10

        if digit > largest_digit:
            largest_digit = digit

        n = n // 10

    return largest_digit


print(largest(152))
