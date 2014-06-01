from utils import to_decimal, substract_binary


def two_complement(binary):
  sign = binary[0]
  binary = substract_binary(binary, '1')
  my_binary = ''.join(['1' if bit == '0' else '0'
                      for bit in binary])
  number = to_decimal(my_binary)
  return number if sign == '0' else number * -1
