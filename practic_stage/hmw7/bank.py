import socket
import time

from messages import builder


class Bank(object):
  def __init__(self, name, host="127.0.0.1", port=6888):
    self.name = name
    self.clients = {}

    self.host = host
    self.port = port

    self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.socket.connect((self.host, self.port))

  def load(self):
    with open('logs/%s.log' % int(time.time())) as f:
      content = f.read()
      for transaction in content.split("\n"):
        self.load_transaction(transaction)

  def add(self, client, money):
    self.client[client] = {
        'money': money
    }

  def pay(self, client, to, how_much):
    message = builder('transfer', client, to, how_much, int(time.time()))
    self.socket.send(message)
