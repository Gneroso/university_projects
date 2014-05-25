import struct
import socket


class Peer(object):
  def __init__(self, host, port, peer_id, torrent):
    self.host = host
    self.port = int(port)

    self.torrent = torrent
    self.peer_id = peer_id

    self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  def handshake(self):
    self.socket.connect((self.host, self.port))

    message = struct.pack("!i19sh40s20s", 19, 'BitTorrent protocol', 0x00,
                          self.torrent.hash, self.peer_id)
    self.socket.send(message)

    response = self.socket.recv(2048)
    if response != message:
      socket.close()

    bitfield = self.socket.recv(2048)
    length, id, bitfield = struct.unpack("!hbi", bitfield)
    return bin(bitfield)[2:]

  def request(self, piece, start, end):
    message = struct.pack("!hb", 1, 2)
    self.socket.send(message)

    while True:
      message = self.socket.recv(2048)

      if self.is_unchocked(message):
        message = struct.pack("!hbhhh", 13, 6, piece, start, end - start)
        self.socket.send(message)

      if self.is_block(message):
        self.write_block(message)
        return

  def is_block(self, message):
    length, id = struct.unpack("!hb", message[:3])
    return id == 7

  def write_block(self, message):
    length, id, piece_index, start = struct.unpack("!hbhh", message[:7])
    with open("examples/downloads/testing.part", "w") as f:
      f.seek(start)
      f.write(message[7:])

  def is_unchocked(self, message):
    if not len(message) == 3:
      return False

    length, id = struct.unpack("!hb", message)
    return id == 1

  def __hash__(self):
    return (self.host, self.ip)
