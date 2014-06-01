import json


class Machine(object):
  def __init__(self, coffee_cost, money):
    self.coffee_cost = coffee_cost
    self.money = money

  def can_give_change(self, coffees):
    return False if self.total < coffees * self.coffee_cost else True

  @property
  def total(self):
    return sum([self.money[bill] * int(bill) for bill in self.money])

  def make_coffee(self):
    while True:
      coffees = int(raw_input("How many coffee do you want?: "))

      if not self.can_give_change(coffees):
        message = "Sorry, I can't give you change. Do you want to continue?[Y]"
        answer = raw_input(message)
        if answer not in ['Y', 'y', 'YES', 'yes', 'ye', 'YE']:
          continue

      result = {}
      change = self.coffee_cost * coffees
      for bill in sorted(self.money.keys(), key=lambda key: -1 * int(key)):
        while self.money[bill] > 0 and change > 0 and change >= int(bill):
          change -= int(bill)
          self.money[bill] -= 1
          if bill not in result:
            result[bill] = 1
          else:
            result[bill] += 1
      print "Change " + json.dumps(result)
      print "Remaing" + json.dumps(self.money)
