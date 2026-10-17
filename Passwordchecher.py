
# Password Strength Checker

password = input("Enter your password: ")

has_upper = any(char.isupper() for char in password)
has_lower = any(char.islower() for char in password)
has_digit = any(char.isdigit() for char in password)
has_special = any(not char.isalnum() for char in password)

score = sum([has_upper, has_lower, has_digit, has_special])

print("\n--- PASSWORD ANALYSIS ---")
print("Length:", len(password))

if len(password) >= 8 and score == 4:
    print("Strength: Strong")
elif len(password) >= 6 and score >= 2:
    print("Strength: Medium")
else:
    print("Strength: Weak")

print("Uppercase present:", has_upper)
print("Lowercase present:", has_lower)
print("Digit present:", has_digit)
print("Special character present:", has_special)
