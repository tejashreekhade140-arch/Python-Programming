
def countFreq(n, k):
    freq = {}

    for digit in str(n):
        freq[int(digit)] = freq.get(int(digit), 0) + 1

    result = []

    for digit in freq:
        if freq[digit] >= k:
            result.append(digit)

    return sorted(result)


n = 13464987139
k = 3

print("Number:", n)
print("Minimum Frequency:", k)
print("Digits appearing at least k times:", countFreq(n, k))
