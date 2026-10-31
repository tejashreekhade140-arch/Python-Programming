numbers = [1, 2, 3, 5, 6, 7]

n = len(numbers) + 1

total = n * (n + 1) // 2

missing = total - sum(numbers)

print("Missing Number:", missing)

#Frequency Count of each number 

numbers = [10, 20, 10, 30, 20, 10, 40, 30]

frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print("Element Frequency:")

for num, count in frequency.items():
    print(num, ":", count)

