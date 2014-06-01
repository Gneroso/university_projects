from signed import to_signed_binary


def two_complement(integer):
  return to_signed_binary(integer, '0') if integer >= 0 else negative(integer)


def negative(integer):
  sign = '1'
  positive_integer = to_signed_binary(integer * -1)

  return sign + ''.join(['1' if bit == '0' else '0'
                         for bit in positive_integer[1:]])
