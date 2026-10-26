
print("🎓 STUDENT PRODUCTIVITY TRACKER")
print("-" * 30)

name = input("Enter your name: ")
study_hours = float(input("Hours studied today: "))
tasks = int(input("Tasks completed today: "))

print("\n📊 YOUR DAILY REPORT")
print("Student:", name)
print("Study Hours:", study_hours)
print("Tasks Completed:", tasks)

if study_hours >= 4 and tasks >= 3:
    print("Status: Excellent work! 🔥")
elif study_hours >= 2:
    print("Status: Good job! Keep going 💪")
else:
    print("Status: Try to improve tomorrow 🚀")


