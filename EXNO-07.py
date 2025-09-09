# Simple Student Marksheet Program

# Input student details
name = input("Enter Student Name: ")
roll = input("Enter Roll Number: ")

# Input marks
tam = int(input("Enter Tamil Number: "))
eng = int(input("Enter English Marks: "))
math = int(input("Enter Math Marks: "))
sci = int(input("Enter Science Marks: "))

# Calculate total and percentage
total = tam + eng + math + sci
percentage = total / 4

# Display Marksheet
print("\n===== Student Marksheet =====")
print(f"Name       : {name}")
print(f"Roll No.   : {roll}")
print(f"Tamil No.   : {tam}")
print(f"English    : {eng}")
print(f"Math       : {math}")
print(f"Science    : {sci}")
print("-----------------------------")
print(f"Total      : {total}")
print(f"Percentage : {percentage:.2f}%")

# Grade system
if percentage >= 90:
    grade = "A+"
elif percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 50:
    grade = "C"
else:
    grade = "Fail"

print(f"Grade      : {grade}")
print("=============================")
