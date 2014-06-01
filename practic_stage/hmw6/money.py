import json


class Money(object):
  def __init__(self, money):
    self.content = json.loads(money)

  @property
  def total(self):
    return sum([self.content[bill] for bill in self.content])
