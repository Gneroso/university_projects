from utils import substract_binary


def two_complement(signed):
  signed = substract_binary(signed, '1')
  return signed[0] + ''.join(['1' if bit == '0' else '1'
                              for bit in signed[1:]])
