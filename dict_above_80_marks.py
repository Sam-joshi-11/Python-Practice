# Create empty dictionary
students = {}

# Take input from user
n = int(input("How many students? "))

for i in range(n):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks
print(students)

# Print students who scored above 80
print("\nStudents scoring above 80:")
for name, marks in students.items():
    if marks > 80:
        print(name, "=>", marks)
