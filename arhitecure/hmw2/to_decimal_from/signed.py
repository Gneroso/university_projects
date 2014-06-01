from utils import to_decimal


def signed(binary):
  sign = binary[0]
  number = to_decimal(binary[1:])

  return number if sign == '0' else number * -1
