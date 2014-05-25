import struct
import socket

from messages import parser, builder


class Peer(object):
  def __init__(self, host, port, peer_id, torrent):
    self.host = host
    self.port = int(port)

    self.torrent = torrent
    self.peer_id = peer_id

    self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.socket.connect((self.host, self.port))

  @property
  def handshake(self):
    message = struct.pack("!i19sh40s20s", 19, 'BitTorrent protocol', 0x00,
                          self.torrent.hash, self.peer_id)
    self.socket.send(message)

    response = self.socket.recv(2048)
    if response != message:
      self.socket.close()
      return False
    return True

  @property
  def bitfield(self):
    if not self.handshake:
      return

    bitfield = self.socket.recv(2048)
    return parser(bitfield)[1]

  def request(self, piece, start, length):
    self.socket.send(builder('interested'))

    while True:
      message = parser(self.socket.recv(400000))
      if not message:
        continue

      if message[0] == 'unchoke':
        self.socket.send(builder('request', piece, start, length))

      if message[0] == 'piece':
        self.write_block(message[1])
        return

  def write_block(self, message):
    length, id, index, start, content = message
    BLOCK_SIZE = 2 ** 14
    blocks_per_piece = (self.torrent['info']['length'] / 10) / BLOCK_SIZE
    with open("examples/downloads/testing4.part", "w") as f:
      offset = index * blocks_per_piece * BLOCK_SIZE
      f.seek(start * BLOCK_SIZE + offset)
      f.write(content)

  def is_unchocked(self, message):
    if not len(message) == 3:
      return False

    length, id = struct.unpack("!hb", message)
    return id == 1
