from utils import add_two_binary

from .signed import to_signed_binary
from .one_complement import negative as negative_one


def two_complement(integer):
  return to_signed_binary(integer, '0') if integer >= 0 else negative(integer)


def negative(integer):
  number = negative_one(integer)[1:]
  return add_two_binary(number, '1')
