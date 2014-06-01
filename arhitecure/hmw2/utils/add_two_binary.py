def add_two_binary(first, second):
  first = first[::-1] if len(first) >= len(second) else second[::-1]
  second = second[::-1] if len(first) >= len(second) else first[::-1]
  third = []

  carry = 0
  for index, second_bit in enumerate(second):
    result = int(second_bit) + int(first[index]) + carry
    carry = result / 2

    third.append(str(result % 2))

  index += 1

  while index < len(first):
    result = int(first[index]) + carry
    carry = result / 2
    third.append(str(result % 2))
    index += 1

  if carry:
    third.append(str(carry))

  return ''.join(third)[::-1]
