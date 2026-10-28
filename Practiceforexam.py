"""
marks=[2,3,4,5,6]
avg= sum(marks)/len(marks)
print(avg)

nm = input("Enter your name ") 
age= input ("enter your age ") 
print(nm,age,sep=" with ") 
age = int(input ("Enter age ")) 
print ("After 20 years you are at ", age+20) 
print (type(nm)) 
print(type(age)) 

name="Tejashree"
subject="python"
message=f" hello {name} welcome to {subject} class"
print(message)

#Boolean
score=50
passed=score >=30
print("passed" if passed else "fails")

#sequence data
Student=['tejashree','Soummya','ankita','priti'] #list
info = (101,'2026-08-16','MCAI')
subjects={"python",'ADBMSss',"DDSA"}
print(Student)
print(info)
print(subjects)


#Dictionries
student={
    101:{"Name":"aditi","Scores":[89,80]},
    102:{"Name":"Pari","Scores":[76,98]}
}
for sid ,details in student.items():
    avg=sum(details["Scores"])/len(details["Scores"])
    passed=avg>=50
    print(details["Name"],"average:",avg,"Passed"if passed else"Fail")
    msg=f"stuent name:{details['Name']} Scores:{avg} marks"
    print(msg)
"""
#sequence data type with append,slicing and range
#list (mutable sequence)
students=["aditi","rahul","snheka"]
print("list of students:",students)
students.append("karan") # add new element

print("list:",students)
print("first student:",students[0])

#Tuple (immutable Sequence)
student_info=(101,"aditi","MCAI",)
print("\n tuple:",student_info)
print("\nstudent id:",student_info[0])

#range(sequence of numbers)
numbers=range(1,5)
print("\nrange:",list(numbers))

#demostrating Slicing
print("\nSlicing:",students[:2])

#Iterating Through a sequence
print("\nTuple:")
for i in student_info:
    print(i)

#Range Datatype
#in step of three
for i in range(1,10,3):
    print(i)
#count down
for i in range(5,0,-1):
    print(i)

#For LOOp
for i in range(1,5):
    print("*" *i)

# sum of first N numbers
n=int(input("Enter your number:"))
total=0
for i in range(1,n+1):
    total+=i
print(total)