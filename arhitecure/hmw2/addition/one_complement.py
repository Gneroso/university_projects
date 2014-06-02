from utils import add_two_binary


def one_complement(first, second):
  result = add_two_binary(first, second)
  if len(result) > 8:
    result = add_two_binary(first, '1')
  return result
