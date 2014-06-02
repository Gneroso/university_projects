import cli.log

from to_decimal_from import (signed as signed_to_decimal,
                             one_complement as one_complement_to_decimal,
                             two_complement as two_complement_to_decimal,
                             excess as excess_to_decimal)

from from_signed import (one_complement as to_one_complement,
                         two_complement as to_two_complement,
                         excess as to_excess)

from from_one_complement_to import (signed as from_one_to_signed,
                                    two_complement as from_one_to_two_complement,
                                    excess as from_one_to_excess)

from from_two_complement_to import (signed as from_two_to_signed,
                                    one_complement as from_two_to_one_complement,
                                    excess as from_two_to_excess)
from from_decimal_to import signed, one_complement, two_complement, excess


@cli.log.LoggingApp
def transform(app):
  _from = getattr(app.params, 'from')
  number = app.params.number
  to = app.params.to

  if _from == 'decimal':
    if to == 'signed':
      print signed(int(number))
    if to == 'one':
      print one_complement(int(number))
    if to == 'two':
      print two_complement(int(number))
    if to == 'excess':
      print excess(int(number))

  if _from == 'signed':
    if to == 'decimal':
      print signed_to_decimal(number)
    if to == 'one':
      print to_one_complement(number)
    if to == 'two':
      print to_two_complement(number)
    if to == 'excess':
      print to_excess(number)

  if _from == 'one':
    if to == 'decimal':
      print one_complement_to_decimal(number)
    if to == 'signed':
      print from_one_to_signed(number)
    if to == 'two':
      print from_one_to_two_complement(number)
    if to == 'excess':
      print from_one_to_excess(number)

  if _from == 'two':
    if to == 'decimal':
      print two_complement_to_decimal(number)
    if to == 'signed':
      print from_two_to_signed(number)
    if to == 'one':
      print from_two_to_one_complement(number)
    if to == 'excess':
      print from_two_to_excess(number)


transform.add_param("number", help="Specific the number to transform",
                    type=str)

transform.add_param("-f", "--from", help="Specific the base or representation"
                    "in which the number is given")

transform.add_param("-t", "--to", help="Specific the base in which the"
                    "number will be tranformed")

if __name__ == "__main__":
  transform.run()
