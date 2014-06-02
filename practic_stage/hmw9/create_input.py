import json


routes = {
    'A': [('B', 5), ('E', 1)],
    'B': [('C', 10), ('E', 1)],
    'C': [('B', 1), ('D', 5)],
    'D': [('C', 2), ('E', 4), ('F', 1)],
    'E': [('C', 3), ('F', 6), ('G', 1), ('B', 1)],
    'F': [('E', 4), ('G', 2)],
    'G': [('A', 3)]
}

with open("input", "w") as f:
  f.write(json.dumps(routes))
