if True:
    print("Inside Block")
print("Outside Block")

# if else statements
n= int(input("Enter Values:"))
if n >0:
    print("positive")
elif n==0:
    print("Zero")
else:
    print("Negative")

#while loop
count=0
while count<5:
    print(count)
    count+=1

#for control Keywords

#continue- skips current iteration
for i in range(5):
    if i==2:
        continue
    print(i)
#Break - exits loop immediatly
for i in range(5):
    if i==3:
        break
    print(i)

#loop else
for i in range(5):
    print(i)
else:
    print("Loop finished without break")

