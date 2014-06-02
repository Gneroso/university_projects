def two_complement(first, second):
  first = first[::-1]
  second = second[::-1]
  borrows = [0]
  third = []

  borrowed = 0
  for index, second_bit in enumerate(second):
    result = int(first[index]) - int(second_bit) - borrowed
    if result < 0:
      borrowed = 1
      result *= -1
    else:
      borrowed = 0
    borrows.append(borrowed)

    third.append(str(result))

  index += 1

  while index < len(first):
    result = int(first[index]) - borrowed
    if result < 0:
      borrowed = 1
      result *= -1
    else:
      borrowed = 0
    borrows.append(borrowed)

    third.append(str(result))
    index += 1

  if borrows[len(borrows) - 1] != borrows[len(borrows) - 2]:
    raise ValueError("Overflow")

  return ''.join(third)[::-1]
