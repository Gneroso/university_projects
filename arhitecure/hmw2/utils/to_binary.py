def to_binary(integer):
  integer = integer * -1 if integer < 0 else integer

  number = ''
  while integer:
    number += str(integer % 2)
    integer /= 2

  return number
