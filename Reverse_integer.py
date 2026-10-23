
def reverseInteger(x):
    sign = -1 if x < 0 else 1

    reverse = int(str(abs(x))[::-1]) * sign

    if reverse < -2**31 or reverse > 2**31 - 1:
        return 0

    return reverse


num = 123

print("Original Number:", num)
print("Reversed Number:", reverseInteger(num))
