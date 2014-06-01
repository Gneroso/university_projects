from to_decimal_from import one_complement as to_decimal_from_one_complement
from from_decimal_to import excess as from_decimal_to_excess


def excess(one_complement):
  decimal = to_decimal_from_one_complement(one_complement)
  return from_decimal_to_excess(decimal)
