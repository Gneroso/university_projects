import json
from random import randint


money = [10, 50, 100, 500]

with open("input", "w") as f:
  f.write(json.dumps({bill: randint(1, 100) for bill in money}))
