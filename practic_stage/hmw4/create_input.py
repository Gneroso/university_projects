from random import randint
import json


fields = ['c', 'c++', 'algorithms', 'data structures']


students = [{
    'name': 'Vlad Temian',
    'age': 20,
    'id': 1931115350016,
    'grades': {field: randint(1, 10) for field in fields}
}, {
    'name': 'Ion Arton',
    'age': 20,
    'id': 1921315451016,
    'grades': {field: randint(1, 10) for field in fields}

}]

with open("input", "w") as f:
  f.write(json.dumps(students))
