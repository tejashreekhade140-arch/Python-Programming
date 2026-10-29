"""
#Frequency Count
text=input("Enter String:")
freq={}
for i in text:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print(freq)

#Find Duplicate elements in a list
number=[10,20,30,10,40,40]
dup=[]
for i in number:
    if number.count(i)>1 and i not in dup:
        dup.append(i)
print(dup)

#find second Largest number in a list
number=[20,30,44,55,81,199]
uni_num=sorted(set(number))
if len(uni_num)>=2:
    print("Second Largest:",uni_num[-2])
else:
    print(No)

# Check whether a string is a palindrome
text=input("Enter a String:")
text=text.lower().replace(" ","")
if text==text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
# Count Vowels and Consonants
text=input("Enter a String:")
Vowels=0
Consonants=0
for i in text:
    if i in "aeiou":
        Vowels+=1
    else:
        Consonants+=1
print(Vowels)
print("Consonants",Consonants)

#Prime Numbers
n=int(input("Enter a Number"))
for i in range(2,n+1):
    Prime=True
    for j in range(2,i):
        if i % j==0:
            Prime=False
            break
    if Prime:
        print(i,end=" ")

# Separate Even and Odd numbers into two Lists
numbers=[10,2,4,3,5,1,9,11,1,13]
even=[]
odd=[]
for i in numbers:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("Even:",even)
print("Odd:",odd)



def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

print(is_prime(7))
print(is_prime(10))
"""
#count odd digits
def Odd_Digits(n):
    count=0
    for i in str(abs(n)):
        if int(i) % 2!=0:
            count+=1
    return count
print(Odd_Digits(1245))

#Reverse an integer
def reverse(n):
    reverse=-1 if n<0 else 1
    return reverse*int(str(abs(n))[::-1])
print(reverse(234512))

#palindrome
def palindrome(n):
    return str(n)==str(n)[::-1]
print(palindrome(676))

#OR

def palindrome(n):
    if str(n)==str(n)[::-1]:
        print("Is palindrome")
    else:
        print("Not Palindrome")
palindrome(676)

#Return Largest Digit in a number
def largest(n):
    return max(str(abs(n)))
print(largest(234598))

#Armstrong Number
def armstrong(n):
    digit=str(n)
    length=len(digit)
    total=0
    for i in digit:
        total+=int(i)**length
    return total==n
print(armstrong(153))

#Prime Number
def prime(n):
    if n<2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i==0:
            return False
    return True
print(prime(11))
print(prime(2))

"""
#Count of Prime Numbers
def count_prime(n):
    count=0
    if n>0:
        is_prime=True
    for i in range(2,n+1):
        if n%i==0:
            is_prime=False
            count+=1
    return count
print(count_prime(7))
"""