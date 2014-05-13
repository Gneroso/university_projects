#!/usr/bin/env python
import struct

from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

from announce.torrent import Torrent


class Announce(DatagramProtocol):

  def parse_connection(self, data):
    connection, action, transaction_id = struct.unpack("!qii", data)
    message = struct.pack('!iiq', action, transaction_id, connection)
    return message

  def parse_announce(self, data, host, port):
    connection_id, action, transaction_id, info_hash, peer_id, downloaded, \
    left, uploaded, event, ip, key, num_want, \
    port = struct.unpack("!qii40s20sqqqiIIiH", data)

    torrent = Torrent(info_hash)

    if not torrent.can_announce(peer_id):
      error_message = "You need to wait 5 minutes to reannounce yourself"
      response = struct.pack('!ii%ss' % len(error_message), action,
                             transaction_id, error_message)
    else:
      torrent.peers = "%s:%s" % (host, port)
      torrent.set_announce(peer_id)
      response = struct.pack('!iiiii', action, transaction_id, 5 * 60,
                             torrent.leechers, torrent.seeders)
      response += torrent.binary_peers

    return response

  def datagramReceived(self, data, (host, port)):
    if len(data) < 90:
      data = self.parse_connection(data)
    else:
      data = self.parse_announce(data, host, port)

    self.transport.write(data, (host, port))

reactor.listenUDP(9999, Announce())
reactor.run()
