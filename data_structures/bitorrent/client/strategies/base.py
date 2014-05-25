from abc import ABCMeta, abstractmethod


class Strategy(object):
  __metaclass__ = ABCMeta

  def __init__(self, pieces, torrent):
    self.pieces = pieces
    self.torrent = torrent

  @abstractmethod
  def build(self):
    raise NotImplemented("A strategy must have a build method")
