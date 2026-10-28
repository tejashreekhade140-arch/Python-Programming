#python examples for common string functions

#sample String
text="  Welcome to IMCC !   "

print(text)

# 1. strip spaces from both ends
print("remove spaces:",text.strip())

# 2. converts to lowercase
print("Lower Case:",text.lower())

# 3. converts to uppercase
print("Upper Case:",text.upper())

# 4. capitalize First letter
text=text.strip()
print("Capitalize first letter:",text.capitalize())

# 5. title- capitalize each words first letter
print(text.title())

# 6. Count occurence of substring 
print("Letter C occurs ",text.count("C"),"times in text")

# 7. find the position of a substring (-1 if not fount)
print("position of IMCC in text is:",text.find("IMCC"))

# 8.replace a substring 
print(text.replace("IMCC","Python Magic"))

# 9. check if string starts or ends with certain substring they do not concedered a spaces 
print(text.startswith("We"))
print(text.endswith("!   "))

# 10. Split string into list by a delimeter
print("Simple Split",text.split())

# 11. join a list of strings with a separate 
words=["python","is","fun"]
print(" ".join(words))

# 12.check if string is alphanumeric,alphabetic or numeric
print(text.isalnum())
print("abc123".isalnum())
print(text.isalpha())
print("abc".isalpha())
print("123".isdigit())

# 13. Swap case (Uppercase to Lowercase and vice versa)
print(text.swapcase())
print("Hello World".swapcase())

#14. Partition a string into 3 parts (before, separator, after)
print(text.partition("come"))
print("Hello".partition("ll"))

# 15.Expand tabs to spaces
tab_text="hello\tpython"
print(tab_text.expandtabs(tabsize=4))

# 16.Check is string contains only whitespace
print("  ".isspace())

# 17. Zero-fill on the left
print("42".zfill(5))

# 18. Encode string to bytes
print(text.encode())
print(" hello ".encode())

# 19. sorting
print(sorted(text))
print(sorted("Tejashree"))

