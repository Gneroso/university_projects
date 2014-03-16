import time

from utils import yellow, green, blue, mangenta, red


class Convert(object):
  vocabulary = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

  def __init__(self, number, _from, to, log):
    self.log = log

    self.number = number
    self._from = _from
    self.to = to

  def run(self):
    self.log.info("Start transforming %s from base %s to base %s" %
                  (self.number, self._from, self.to))
    if self._from != 10:
      self.log.warn(yellow("Initial base is not decimal!"))
      now = time.time()
      self.number = self.to_decimal(self.number, self._from)
      self.log.debug(blue("Transforming the number from base %s into decimal"
                          " took %f seconds" % (self._from,
                                                round(time.time() - now, 10))))
      self.log.info("Decimal representation of the number is %s" % self.number)

    if self.to != 10:
      self.log.debug(blue("Transforming the number from base %s into base %s"
                          " took %f seconds" % (self._from, self.to,
                                                round(time.time() - now, 10))))
      self.number = self.to_base(self.number, self.to)

    print green("Your number is %s" % red(self.number))

  def to_decimal(self, number, _from):
    number = number[::-1]
    new_number = 0
    digits = self.digits(_from)

    for index in xrange(len(number)):
      value = digits.index(number[index])
      digit = int(value) * (self._from ** index)

      self.log.debug(mangenta("%s * (%s ** %s) = %s + %s = %s" %
                          (value, self._from, index, digit, new_number,
                           new_number + digit)))

      new_number += digit

    return new_number

  def to_base(self, number, to):
    number = int(number)
    new_number = ''
    digits = self.digits(to)

    while number > to:
      new_number += digits[number % to]
      number /= to

    if number != 0:
      new_number += str(number)
    return new_number[::-1]

  def digits(self, radix):
    if radix < 2 or radix > 62:
      self.log.error("Radix base should be between 2 and 62, not %s" % radix)
      raise ValueError("Radix base should be between 2 and 62, not %s" % radix)

    return self.vocabulary[:radix]
