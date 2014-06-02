from copy import deepcopy
import json


with open("input") as f:
  routes = json.loads(f.read())

solutions = []


def is_solution(possible):
  if len(possible) == len(routes):
    for node in routes[possible[-1]]:
      if node[0] == possible[0]:
        return True
  return False


def backtrack(current, cost, solution):
  for route in routes[current]:
    if route[0] not in solution:
      solution.append(route[0])
      if is_solution(solution):
        for node in routes[solution[-1]]:
          if node[0] == solution[0]:
            solution.append(node[0])
            solutions.append((solution, cost + route[1] + node[1]))
      backtrack(route[0], cost + route[1], deepcopy(solution))

for node in routes:
  backtrack(node, 0, [node])

print sorted(solutions, key=lambda key: key[1])
