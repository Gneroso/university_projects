import urllib
from random import randint
from urlparse import urlparse

from torrent import Torrent
from trackers.udp import UDPTracker


class Client(object):
  __TORRENTS = {}

  def __init__(self):
    self.peer_id = urllib.quote("-AZ2470-" + "".join([str(randint(0, 9)) for i in xrange(12)]))

  @property
  def torrents(self):
    return self.__TORRENTS

  @torrents.setter
  def torrents(self, new_torrent):
    self.__TORRENTS[new_torrent] = Torrent(new_torrent)

  def _get_peers(self, torrent):
    peers = {}

    for url in torrent.urls:
      parsed = urlparse(url)
      if parsed.scheme == 'udp':
        _, url, port = url.split(":")
        tracker = UDPTracker(url[2:], int(port), torrent, self.peer_id)

        peers.update({ip: port for ip, port in tracker.peers})

    return peers

  def download(self, torrent):
    if not torrent in self.__TORRENTS:
      raise ValueError('%s not here' % torrent)

    torrent = self.__TORRENTS[torrent]
    peers = self._get_peers(torrent)
    print peers
