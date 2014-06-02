import json


routes = {
    'A': [('B', 8), ('C', 2)],
    'B': [('C', 5), ('A', 4)],
    'C': [('A', 1), ('B', 2)]
}

with open("input", "w") as f:
  f.write(json.dumps(routes))
