# 1.Write a program to rad a file and count how many vowels are present in its content.
with open("Data.txt","r")as f:
    content=f.read()
    count = 0
    for i in content:
        if i.lower() in "aeiou":
            count +=1
    print("Count of Vowels in a file:",count)
