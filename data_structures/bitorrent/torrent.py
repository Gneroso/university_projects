import hashlib
import urllib

import bencode


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
  def urls(self):
    urls = [self.decoded['announce']]
    urls += [announce[0] for announce in self.decoded['announce-list']]

    return urls
