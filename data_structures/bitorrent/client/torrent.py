import hashlib

import bencode


class Torrent(object):

  def __init__(self, path):
    self.encoded = self._get_meta(path)
    self.decoded = bencode.bdecode(self.encoded)

  def _get_meta(self, path):
    with open(path) as f:
      return f.read()

  def __getitem__(self, item):
    return self.decoded[item]

  @property
  def hash(self):
    info_hash = hashlib.sha1(bencode.bencode(self.decoded['info'])).hexdigest()
    return info_hash

  @property
  def urls(self):
    urls = [self.decoded['announce']]
    if 'announce-list' in self.decoded:
      urls += [announce[0] for announce in self.decoded['announce-list']]
    print urls

    return urls
