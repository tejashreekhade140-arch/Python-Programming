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

#pop removes last item
last_color=colors.pop()
print(last_color)

#adding of items at last and at specific location
#at last
colors=["red","blue"]
colors.append("Black")
print(colors)

#At specific position
colors.insert(2,"Pink")
print(colors)

#function performed on list
#length
numbers=[1,2,9,4,5,3,6,7,8]
print(len(numbers))

#sum
print(sum(numbers))

#sorting
print(sorted(numbers))
print(sorted(numbers,reverse=True))
