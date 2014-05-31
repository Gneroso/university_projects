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
print students

students.sort_by("c")
print students
