
def sumOfFrequencies(arr):
    freq = {}

    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    result = max(freq.values()) + min(freq.values())
    print(result)


sumOfFrequencies([1, 2, 2, 3, 3, 3])
