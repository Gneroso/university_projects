import time


class Bank(object):
  def __init__(self, name):
    self.name = name
    self.clients = {}

  def load(self):
    with open('logs/%s.log' % int(time.time())) as f:
      content = f.read()
      for transaction in content.split("\n"):
        self.load_transaction(transaction)
