from urlparse import urlparse

from torrent import Torrent
from trackers.udp import UDPTracker


class Client(object):
  __TORRENTS = {}

  @property
  def torrents(self):
    return self.__TORRENTS

  @torrents.setter
  def torrents(self, new_torrent):
    self.__TORRENTS[new_torrent] = Torrent(new_torrent)

  def download(self, torrent):
    if not torrent in self.__TORRENTS:
      raise ValueError('%s not here' % torrent)

    torrent = self.__TORRENTS[torrent]
    for url in torrent.urls:
      parsed = urlparse(url)
      if parsed.scheme == 'udp':
        _, url, port = url.split(":")
        tracker = UDPTracker(url[2:], int(port), torrent)
        print tracker.peers
