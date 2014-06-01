def signed(integer):
  sign = '1' if integer < 0 else '0'
  integer = integer * -1 if integer < 0 else integer

  number = ''
  while integer:
    number += str(integer % 2)
    integer /= 2

  if len(number) >= 8:
    number = number[:8]
    return number[::-1]

  while len(number) < 7:
    number += '0'

  return sign + number[::-1]
