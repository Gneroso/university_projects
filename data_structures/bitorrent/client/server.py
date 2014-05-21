import struct
from gevent.server import StreamServer

from unipath import Path

from torrent import Torrent


def has_torrent(info_hash):
  for obj in Path('examples/').walk():
    if obj.isdir():
      continue

    torrent = Torrent(obj)

    if torrent.hash == info_hash:
      return True
  return False


def handshake(data, socket):
  pstrlen, pstr, reserved, info_hash, peer_id = struct.unpack("!i19sh40s20s",
                                                              data)

  if not has_torrent(info_hash):
    socket.close()
    return

  socket.send(data)


def handle(socket, address):
  while True:
    data = socket.recv(2048)
    if not data:
      print "Client disconnected"
      break

    if len(data) == 85:
      handshake(data, socket)


server = StreamServer(('127.0.0.1', 6888), handle)
server.serve_forever()
