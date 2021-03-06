#/usr/bin/env python
import cli.log

from conversion import Convert


@cli.log.LoggingApp
def transform(app):
  _from = getattr(app.params, 'from')
  number = app.params.number
  to = app.params.to

  convert = Convert(number, _from, to, app.log)
  convert.run()

transform.add_param("number", help="Specific the number to transform",
                    type=str)

transform.add_param("-f", "--from", help="Specific the base in which the"
                    "number is given", type=int)

transform.add_param("-t", "--to", help="Specific the base in which the"
                    "number will be tranformed", type=int)

if __name__ == "__main__":
  transform.run()
