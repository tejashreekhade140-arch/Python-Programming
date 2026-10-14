# 3. Take a sentence from the user, split it into words, and store them in a list. Print the longest word.

sentence = input("Enter a sentence: ")
words = sentence.split()
print("List of words:", words)
if words:
    longest = max(words, key=len)
    print("Longest word:", longest)
    print("Length:", len(longest))
else:
    print("No words entered")
