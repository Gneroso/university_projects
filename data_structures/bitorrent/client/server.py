import struct

from bencode import bdecode
from gevent.server import StreamServer
from unipath import Path

from torrent import Torrent
from messages import parser, builder


def get_bitfield(torrent):
  filename = torrent.path.stem
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
      return torrent
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
  message = builder('bitfield', get_bitfield(torrent))

  socket.send(message)
  return torrent


def parse_request(socket, torrent, piece_index, start, block_length):
  BLOCK_SIZE = 2 ** 14
  blocks_per_piece = (torrent['info']['length'] / 10) / BLOCK_SIZE
  with open("examples/file.txt") as f:
    offset = piece_index * blocks_per_piece * BLOCK_SIZE
    f.seek(start * BLOCK_SIZE + offset)
    content = f.read(block_length)

  socket.send(builder('piece', piece_index, start, content))


def handle(socket, address):
  torrent = None
  while True:
    data = socket.recv(2048)
    if not data:
      print "Client disconnected"
      break

    if len(data) == 85:
      torrent = handshake(data, socket)
      continue

    message = parser(data)

    if message[0] == 'interested':
      message = builder('unchoke')
      socket.send(message)

    if message[0] == 'request':
      parse_request(socket, torrent, *message[1])


server = StreamServer(('127.0.0.1', 6888), handle)
server.serve_forever()
