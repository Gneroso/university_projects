import struct
import socket


class TcpPeer(object):
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
      self.socket.close()
