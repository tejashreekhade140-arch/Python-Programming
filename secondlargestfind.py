
numbers = [10, 25, 5, 80, 45, 60]

largest = second_largest = float('-inf')

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num

    elif num > second_largest and num != largest:
        second_largest = num

if second_largest == float('-inf'):
    print("Second largest number does not exist")
else:
    print("Largest Number:", largest)
    print("Second Largest Number:", second_largest)
