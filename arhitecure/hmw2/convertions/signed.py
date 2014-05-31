def signed(integer):
  if integer > 128 or integer < -127:
    raise ValueError("Integer needs to be between -127 and 128")

  sign = '1' if integer < 0 else '0'

  number = ''
  while integer:
    number += str(integer % 2)
    integer /= 2

  while len(number) != 7:
    number += '0'

  return sign + number[::-1]
