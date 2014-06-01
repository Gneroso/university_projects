from utils import to_binary


def excess(integer):
  number = to_binary(integer)[::-1]
  while len(number) < 8:
     number = '0' + number

  return number
