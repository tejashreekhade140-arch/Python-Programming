
def secondHighestOccurringElement(arr):
    freq = {}

    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    frequencies = sorted(set(freq.values()), reverse=True)

    if len(frequencies) < 2:
        print(-1)
        return

    second_freq = frequencies[1]
    result = min(num for num in freq if freq[num] == second_freq)

    print(result)


secondHighestOccurringElement([1, 2, 2, 3, 3, 3])
