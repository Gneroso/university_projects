#!/usr/bin/env python
import struct

from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor


class Announce(DatagramProtocol):

  def parse_connection(self, data):
    connection, action, transaction_id = struct.unpack("!qii", data)
    message = struct.pack('!iiq', action, transaction_id, connection)
    return message

  def parse_announce(self, data):
    message = struct.unpack("!qii20s20sqqqiIIiH", data)
    print message
    return message

  def datagramReceived(self, data, (host, port)):
    if len(data) < 90:
      data = self.parse_connection(data)
    else:
      data = self.parse_announce(data)

    self.transport.write(data, (host, port))

reactor.listenUDP(9999, Announce())
reactor.run()
