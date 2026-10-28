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