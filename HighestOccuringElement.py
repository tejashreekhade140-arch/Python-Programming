
def highestOccurringElement(nums):
    freq = {}

    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    max_freq = max(freq.values())

    result = min(num for num in freq if freq[num] == max_freq)
    print(result)


highestOccurringElement([1, 2, 2, 3, 3, 3])
