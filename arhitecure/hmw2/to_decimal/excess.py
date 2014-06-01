from utils import to_decimal


def excess(binary):
  number = to_decimal(binary)
  return number - 127
