import urllib
import traceback
from random import randint
from urlparse import urlparse

from torrent import Torrent
from trackers.udp import UDPTracker
from trackers.tcp import TCPTracker

from peers import TcpPeer


class Client(object):
  __TORRENTS = {}

  def __init__(self):
    self.peer_id = urllib.quote("-AZ2470-" + "".join([str(randint(0, 9))
                                                     for i in xrange(12)]))

  @property
  def torrents(self):
    return self.__TORRENTS

  @torrents.setter
  def torrents(self, new_torrent):
    self.__TORRENTS[new_torrent] = Torrent(new_torrent)

  def _get_peers(self, torrent):
    peers = []

    for url in torrent.urls:
      parsed = urlparse(url)
      if parsed.scheme == 'udp':
        url = "%s%s" % (parsed.netloc.split(':')[0], parsed.path)
        port = parsed.port
        tracker = UDPTracker(url, int(port), torrent, self.peer_id)
      elif parsed.scheme == 'http':
        tracker = TCPTracker(url, 80, torrent, self.peer_id)

      peers += tracker.peers

    return set(peers)

  def download(self, torrent):
    if torrent not in self.__TORRENTS:
      raise ValueError('%s not here' % torrent)

    torrent = self.__TORRENTS[torrent]
    try:
      # peers = self._get_peers(torrent)
      #  print peer
      peers = [(u'127.0.0.1', u'6888')]
      for peer in peers:
        tcp_peer = TcpPeer(peer[0], peer[1], self.peer_id, torrent)
        tcp_peer.handshake()
    except ValueError as e:
      print traceback.format_exc()
      print e
