# Step 1: Create a dictionary of students and their marks
students = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78,
    "David": 92
}

# Step 2: Use a loop to print each student's name and mark
print("Student Marks:")
for name, mark in students.items():
    print(f"{name}: {mark}")

# Step 3: Calculate and print the average mark
total_marks = sum(students.values())
average = total_marks / len(students)

print(f"\nAverage mark of all students: {average:.2f}")

#completion of program