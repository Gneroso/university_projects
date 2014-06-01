from utils import substract_binary


def one_complement(two_complement):
  return substract_binary(two_complement, '1')
