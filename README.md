# grade-calculator 
def calculate_grade(marks):
    total = sum(marks)
    percentage = total / len(marks)

    if percentage >= 90:
        grade = 'A+ excellent '
    elif percentage >= 80:
        grade = 'A best'
    elif percentage >= 70:
        grade = 'B good'
    elif percentage >= 60:
        grade = 'C ok ok'
    elif percentage >= 50:
        grade = 'D try your best'
    else:
        grade = 'F try next time you are fail '

    return total, percentage, grade

# Get user input
subjects = int(input("Enter the number of subjects: "))
marks = []

for i in range(subjects):
    mark = float(input(f"Enter marks for subject {i+1}: "))
    marks.append(mark)

# Function call
total, percentage, grade = calculate_grade(marks)

# Display result
print("\n--- Student Report ---")
print(f"Total Marks: {total}")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")
