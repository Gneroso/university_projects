import time


P = 11
Q = 19

M = P * Q
TIMES = 101


def png(seed):
  seed ^= seed >> 12
  seed ^= seed << 15
  seed ^= seed >> 17

  return seed * 2685821657736338717


def generate(start, end):
  number = str(png(int(time.time() % 100)))
  try:
    number = int(number[2]) * 10 + int(number[3])
    return int(float(number / 100.0) * float(end - start) + start)
  except Exception as e:
    print e
    return generate(start, end)

dis = range(10)
for i in range(100):
  nr = generate(1, 6)
  dis[nr] += 1
  time.sleep(1)

print dis[2]
print dis[1]
