from utils import to_binary


def signed(integer):
  sign = '1' if integer < 0 else '0'
  return to_signed_binary(integer, sign)


def to_signed_binary(integer, sign):
  number = to_binary(integer)

  if len(number) >= 8:
    number = number[:8]
    return number[::-1]

  while len(number) <= 7:
    number += '0'

  return sign + number[::-1]
