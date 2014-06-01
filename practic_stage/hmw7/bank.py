from hashlib import sha1
import socket
import time

from messages import builder, parser


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

  def transfer_from(self, client, to, how_much, times=0):
    if times >= 3:
      return False

    with open("db/clients.txt") as f:
      clients = f.read()
      if client not in clients:
        raise ValueError("%s is not a client" % client)
      if to not in clients:
        raise ValueError("%s is not a client" % to)

    client = sha1(client).hexdigest()
    to = sha1(to).hexdigest()
    message = builder('transfer', client, to, int(how_much), int(time.time()))
    self.socket.send(message)

    response = parser(self.socket.recv(2048))
    if response is not None and response[0] == 'retry':
      time.sleep(1)
      self.transfer_from(client, to, how_much, times + 1)
    elif response is not None and response[0] == 'success':
      return True
