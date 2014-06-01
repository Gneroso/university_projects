from utils import to_binary


def excess(integer):
  integer += 127

  number = to_binary(integer)[::-1]
  while len(number) < 8:
     number = '0' + number

  return number
