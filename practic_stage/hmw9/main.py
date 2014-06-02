import json


with open("input") as f:
  routes = json.loads(f.read())

print routes
