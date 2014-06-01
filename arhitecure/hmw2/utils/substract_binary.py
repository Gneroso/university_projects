def substract_binary(first, second):
  first = first[::-1]
  second = second[::-1]
  third = []

  borrowed = 0
  for index, second_bit in enumerate(second):
    result = int(first[index]) - int(second_bit) - borrowed
    if result < 0:
      borrowed = 1
      result *= -1
    else:
      borrowed = 0

    third.append(str(result))

  index += 1

  while index < len(first):
    result = int(first[index]) - borrowed
    if result < 0:
      borrowed = 1
      result *= -1
    else:
      borrowed = 0

    third.append(str(result))
    index += 1

  return ''.join(third)[::-1]
