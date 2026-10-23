
def countFreq(n, k):
    freq = {}

    for digit in str(n):
        digit = int(digit)
        freq[digit] = freq.get(digit, 0) + 1

    result = []

    for digit in freq:
        if freq[digit] >= k:
            result.append(digit)

    return sorted(result)


n = int(input("Enter a number: "))
k = int(input("Enter minimum frequency: "))

print("Number:", n)
print("Minimum Frequency:", k)
print("Digits appearing at least k times:", countFreq(n, k))
