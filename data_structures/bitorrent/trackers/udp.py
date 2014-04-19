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
      raise ValueError("Invalid connection_id")

    return self.announce(connection_id)

  def announce(self, connection_id):
    action = ACTIONS['announce']
    transaction_id = self.transaction
    return connection_id

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
