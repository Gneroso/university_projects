from gevent.server import StreamServer

from messages import parser


def handle(socket, address):
  print "Startin server..."

  while True:
    data = socket.recv(2048)
    if not data:
      print "Client disconnected"

    message = parser(data)
    print message

server = StreamServer(('127.0.0.1', 6888), handle)
server.serve_forever()
