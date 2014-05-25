import struct

from bencode import bdecode
from gevent.server import StreamServer
from unipath import Path

from torrent import Torrent


def get_bitfield(torrent):
  filename = torrent.stem
  bitfield = 0b0
  with open('examples/progress/%s.progress' % filename) as f:
    progress = bdecode(f.read())
    for part in progress['pieces']:
      bitfield ^= 1 if part else 0
      bitfield = bitfield << 1
    bitfield = bitfield >> 1
  return bitfield


def has_torrent(info_hash):
  for obj in Path('examples/torrents/').walk():
    if obj.isdir():
      continue

    torrent = Torrent(obj)

    if torrent.hash == info_hash:
      return obj
  return False


def handshake(data, socket):
  pstrlen, pstr, reserved, info_hash, peer_id = struct.unpack("!i19sh40s20s",
                                                              data)

  torrent = has_torrent(info_hash)
  if not torrent:
    socket.close()
    return

  # send handshake back
  socket.send(data)
  import time
  time.sleep(1)
  # send bitfield with pieces
  message = struct.pack("!hbi", 6, 5, get_bitfield(torrent))

  socket.send(message)


def unchoke(socket):
  message = struct.pack('!hb', 1, 1)
  socket.send(message)


def parse_request(socket, data):
  length, id, piece_index, start, block_length = struct.unpack("!hbhhh", data)

  with open("examples/file.txt") as f:
    f.seek(start)
    content = f.read(block_length)

  message = struct.pack("!hbhh", 7 + len(content), 7, piece_index, start) + content

  socket.send(message)


def handle(socket, address):
  while True:
    data = socket.recv(2048)
    if not data:
      print "Client disconnected"
      break

    if len(data) == 85:
      handshake(data, socket)
    if len(data) == 3:
      unchoke(socket)
    if len(data) == 9:
      parse_request(socket, data)


server = StreamServer(('127.0.0.1', 6888), handle)
server.serve_forever()
