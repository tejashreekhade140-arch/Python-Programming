# 4.Read a file, split its content into words, and store them in list.
# i.Print the total number of words.
# ii.print all unique words.
f = open("data.txt", "r")
content = f.read()
f.close()
words = content.split()
# i. Total number of words
print("Total number of words:", len(words))
# ii. Print all unique words
unique_words = set(words)
print("Unique words:")
for word in unique_words:
    print(word)
