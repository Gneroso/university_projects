from utils import substract_binary


def signed(two_complement):
  one_complement = substract_binary(two_complement, '1')
  return one_complement[0] + ''.join(['1' if bit == '0' else '0'
                                      for bit in one_complement[1:]])
