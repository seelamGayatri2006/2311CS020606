marks1 = float(input("Enter marks for Subject 1: "))
marks2 = float(input("Enter marks for Subject 2: "))
marks3 = float(input("Enter marks for Subject 3: "))
average_marks = (marks1 + marks2 + marks3) / 3
if average_marks >= 90:
    grade = "A"
elif 80 <= average_marks < 90:
    grade = "B"
elif 70 <= average_marks < 80:
    grade = "C"
else:
    grade = "Fail"
print(f"Average Marks: {average_marks:.2f}")
print(f"Grade: {grade}")