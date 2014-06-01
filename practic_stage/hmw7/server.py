from gevent.server import StreamServer


def handle(socket, address):
  while True:
    data = socket.recv(2048)


server = StreamServer(('127.0.0.1', 6888), handle)
server.serve_forever()
