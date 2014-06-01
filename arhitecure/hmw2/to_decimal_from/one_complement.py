from utils import to_decimal


def one_complement(binary):
  sign = binary[0]
  binary = ''.join(['1' if bit == '0' else '0'
                    for bit in binary])
  number = to_decimal(binary[1:])
  return number if sign == '0' else number * -1
