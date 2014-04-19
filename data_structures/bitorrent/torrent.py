import hashlib
import urllib
from urlparse import urlparse

import bencode

from trackers.udp import UDPTracker


class Torrent(object):

  def __init__(self, path):
    self.encoded = self._get_meta(path)
    self.decoded = bencode.bdecode(self.encoded)

  def _get_meta(self, path):
    with open(path) as f:
      return f.read()

  @property
  def hash(self):
    info_hash = hashlib.sha1(bencode.bencode(self.decoded['info'])).digest()
    return urllib.quote(info_hash)

  @property
  def peers(self):
    urls = [self.decoded['announce']]
    urls += [announce[0] for announce in self.decoded['announce-list']]

    for url in urls:
      parsed = urlparse(url)
      if parsed.scheme == 'udp':
        _, url, port = url.split(":")
        tracker = UDPTracker(url[2:], int(port), self)
        print tracker.peers
