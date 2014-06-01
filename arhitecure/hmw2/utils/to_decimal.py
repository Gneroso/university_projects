def to_decimal(binary):
  number = 0

  for index, bit in enumerate(binary[::-1]):
    number += int(bit) * (2 ** index)

  return number
