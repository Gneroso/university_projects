def to_binary(integer):
  integer = int(integer)
  integer = integer * -1 if integer < 0 else integer

  number = ''
  while integer:
    number = number + str(int(integer) % 2)
    integer /= 2

  return number
