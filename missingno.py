numbers = [1, 2, 3, 5, 6, 7]

n = len(numbers) + 1

total = n * (n + 1) // 2

missing = total - sum(numbers)

print("Missing Number:", missing)
