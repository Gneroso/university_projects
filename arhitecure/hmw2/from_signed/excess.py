from to_decimal_from import signed as to_decimal_from_signed
from from_decimal_to import excess as from_decimal_to_excess


def excess(signed):
  decimal = to_decimal_from_signed(signed)
  return from_decimal_to_excess(decimal)
