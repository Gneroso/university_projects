def one_complement(integer):
  return positive(integer) if integer >= 0 else negative(integer)


def positive(integer):
  sign = '0'
  number = ''

  while(integer):
    number += str(integer % 2)
    integer /= 2

  if len(number) >= 8:
    number = number[:8]
    return number[::-1]

  while len(number) <= 7:
    number += '0'

  return sign + number[::-1]


def negative(integer):
  sign = '1'
  positive_integer = positive(integer * -1)

  return sign + ''.join(['1' if bit == '0' else '0'
                         for bit in positive_integer[1:]])
