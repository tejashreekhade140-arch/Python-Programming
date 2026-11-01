#Missing element in a List

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

#first non repeting character 
text = input("Enter a string: ")

for char in text:
    if text.count(char) == 1:
        print("First non-repeating character:", char)
        break
else:
    print("No non-repeating character found")

# Move All zeros to end

numbers = [0, 5, 0, 3, 8, 0, 2]

result = []

for num in numbers:
    if num != 0:
        result.append(num)

zero_count = numbers.count(0)

for i in range(zero_count):
    result.append(0)

print("Original List:", numbers)
print("Updated List:", result)


