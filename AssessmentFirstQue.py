#1. Generate a sequence of odd numbers
def sequence(n):
    seq = []

    for i in range(n, 0, -2):
        if i % 2 != 0:
            seq.append(i)

    return seq


print(sequence(11))
