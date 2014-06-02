from __future__ import absolute_import

import cli.log

from substraction import signed, one_complement, two_complement


@cli.log.LoggingApp
def substraction(app):
  representation = app.params.representation
  first = app.params.first
  second = app.params.second

  try:
    if representation == 'signed':
      print signed(first, second)
    if representation == 'one':
      print one_complement(first, second)
    if representation == 'two':
      print two_complement(first, second)
  except ValueError:
    print "Overflow"

substraction.add_param("first", help="First number",
                       type=str)
substraction.add_param("second", help="Second number",
                       type=str)

substraction.add_param("-r", "--representation",
                       help="Specific the representation in which the number"
                       " is given")

if __name__ == "__main__":
  substraction.run()
