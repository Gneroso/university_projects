import json

from machine import Machine


COFFEE_COST = 50

with open("input") as f:
  machine = Machine(COFFEE_COST, json.loads(f.read()))

while True:
  machine.make_coffee()
