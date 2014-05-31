import json

from student import Student, Students
from strategies import InsertionSort


students = Students(InsertionSort)

with open("input") as f:
  content = json.loads(f.read())
  for student in content:
    students.append(Student(**student))

# sort by total
students.sort()
for student in students:
  print student

students.sort_by("c")
for student in students:
  print student
