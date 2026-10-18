
text = input("Enter text: ")

for char in sorted(set(text)):
    if char != " ":
        print(char, ":", text.count(char))
