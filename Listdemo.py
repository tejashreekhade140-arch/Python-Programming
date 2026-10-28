#Empty List
my_list=[]
print(my_list)

#with items
fruits=["apple","banana","cherry"]
print(fruits)
number=[10,20,30,40,50]
print(number[0])
print(number[-1])
print(number[3])

#append items in a list
colors=["red","black"]
colors.append("green")
print(colors)

#insert at specific position
colors.insert(1,"yellow")
print(colors)

#Remove
print("Before remove:",colors)
colors.remove("red")
print(colors)