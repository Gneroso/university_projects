import random
import socket
import struct

from .base import Tracker

CONNECTION_ID = 0x41727101980
ACTIONS = {
    'connect': 0x0,
    'announce': 0x1,
    'scrape': 0x2
}
BUFFER_SIZE = 2048


class UDPTracker(Tracker):
  def __init__(self, *args, **kwargs):
    super(UDPTracker, self).__init__(*args, **kwargs)
    self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    self.socket.settimeout(3)

    self.info_hash = self.torrent.hash

  @property
  def peers(self):
    connection_id = self.connection
    if connection_id is None:
      return []

    return self.announce(connection_id)

  def announce(self, connection_id):
    peers = []
    offset = 20

    # building UPD request
    action = ACTIONS['announce']
    transaction_id = self.transaction
    left = self.torrent['info']['length']
    downloaded = 0x0
    uploaded = 0x0
    ip = 0x0
    key = 0x0
    event = 0x0
    num_wat = -1
    port = 80

    args = (connection_id, action,
            transaction_id, self.info_hash, self.peer_id,
            downloaded, left, uploaded, event, ip, key,
            num_wat, port)
    message = struct.pack("!qii40s20sqqqiIIiH", *args)

    # send request
    self.socket.sendto(message, (self.url, self.port))

    try:
      data, addr = self.socket.recvfrom(BUFFER_SIZE)
      action = struct.unpack("!iiiii", data[:offset])
    except socket.timeout:
      return []

    # parsing ip and port
    while offset < len(data):
      ip, port = struct.unpack_from("!ih", data[offset:])
      ip = socket.inet_ntoa(hex(ip)[2:].zfill(8).decode('hex'))
      peers.append((ip, str(port)))
      offset += 6

    return peers

  @property
  def connection(self):
    action = ACTIONS['connect']
    transaction_id = self.transaction

    message = struct.pack('!q', CONNECTION_ID)
    message += struct.pack('!i', action)
    message += struct.pack('!i', transaction_id)

    self.socket.sendto(message, (self.url, self.port))
    try:
      data, addr = self.socket.recvfrom(BUFFER_SIZE)
    except socket.timeout:
      return None

    return struct.unpack(">iiq", data)[2]

  @property
  def transaction(self):
    return int(random.randint(0, 255))
