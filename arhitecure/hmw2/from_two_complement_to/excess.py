from to_decimal_from import two_complement as to_decimal_from_two_complement
from from_decimal_to import excess as from_decimal_to_excess


def excess(two_complement):
  decimal = to_decimal_from_two_complement(two_complement)
  return from_decimal_to_excess(decimal)
