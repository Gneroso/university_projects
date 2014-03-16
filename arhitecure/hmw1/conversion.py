import time

from utils import yellow, green, blue, mangenta, red


class Convert(object):
  vocabulary = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

  def __init__(self, number, _from, to, log):
    self.log = log

    self.number = number
    self._from = _from
    self.to = to

  @property
  def is_negative(self):
    return self.number[0] == '-'

  def run(self):
    if self.is_negative:
      if self._from != 10:
        self.log.error(red("I dont know how to convert negative numbers if"
                           " there are not in decimal base"))
        return False
      else:
        number = self.transform_negative()
    else:
      number = self.transform_positive()

    print green("Your number is %s" % red(number))

  def transform_positive(self):
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
      now = time.time()
      self.number = self.to_base(self.number, self.to)
      self.log.debug(blue("Transforming the number from decimal into base %s"
                          " took %f seconds" % (self.to,
                                                round(time.time() - now, 10))))

    return self.number

  def transform_negative(self):
    self.log.info("Start transforming %s from base %s to base %s" %
                  (self.number, self._from, self.to))

    now = time.time()
    number = self.number[1:]
    # TODO: don't use builtin functions
    complement = str(bin(~int(number)))[3:]
    self.log.debug(blue("2's complement of %s is %s" %
                        (self.number, complement)))
    new_number = self.to_base(self.to_decimal(complement, 2), self.to)
    self.log.debug(blue("Transforming the number from decimal into base %s"
                        " took %f seconds" % (self.to,
                                              round(time.time() - now, 10))))
    return new_number

  def to_decimal(self, number, _from):
    number = number[::-1]
    new_number = 0
    digits = self.digits(_from)

    for index in xrange(len(number)):
      value = digits.index(number[index])
      digit = int(value) * (_from ** index)

      self.log.debug(blue("%s * (%s ** %s) = %s + %s = %s" %
                          (value, _from, index, digit, new_number,
                           new_number + digit)))

      new_number += digit

    return new_number

  def to_base(self, number, to):
    number = int(number)
    new_number = ''
    digits = self.digits(to)

    while number >= to:
      self.log.debug(blue("%s / %s = %s   %s" %
                          (number, to, number / to, number % to)))

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
