# 2. Read all Lines from a file into a list. Print the total number of lines and Display the 2nd and 4th line.

f = open("data.txt", "r")
lines = f.readlines()
f.close()
print("Total number of lines:", len(lines))

if len(lines) >= 2:
    print("2nd line:", lines[1].strip())
else:
    print("2nd line does not exist")

if len(lines) >= 4:
    print("4th line:", lines[3].strip())
else:
    print("4th line does not exist")
