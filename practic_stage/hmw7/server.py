from gevent.server import StreamServer

from utils import green, red
from messages import parser, builder


transactions = []


def transfer(message, socket):
  _from, to, how_many, date = message[1:]

  if _from in transactions or to in transactions:
    socket.send(builder('retry'))

  transactions.append(_from)
  transactions.append(to)

  with open("logs/now", 'a') as f:
    f.write("-%s:%s:%s:%s" % (_from, to, how_many, date))

  with open("clients/%s" % _from, 'r+') as f:
    money = int(f.read() or '0')
    f.seek(0)
    f.write(str(money - int(how_many)))
    f.truncate()

  with open("clients/%s" % to, 'r+') as f:
    money = int(f.read() or '0')
    f.seek(0)
    f.write(str(money + int(how_many)))
    f.truncate()

  transactions.remove(_from)
  transactions.remove(to)

  socket.send(builder('success'))


def handle(socket, address):
  print green("Client connected")

  while True:
    data = socket.recv(2048)
    if not data:
      print red("Client disconnected")
      return

    message = parser(data)
    if message is None:
      return

    if message[0] == 'transfer':
      transfer(message[1], socket)


server = StreamServer(('127.0.0.1', 6888), handle)
server.serve_forever()
