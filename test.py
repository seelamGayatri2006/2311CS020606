student = {
  1: {"name": "google", "age": 20},
  2: {"name": "Max", "age": 23},
  3: {"name": "jack", "age": 25},
  4: {"name": "mick", "age": 27},
  5: {"name": "dili", "age": 30},
}

# Example of accessing the data
for student_id, details in student.items():
    print(f"Student ID: {student_id}, Name: {details['name']}, Age: {details['age']}")
