from abc import ABCMeta, abstractmethod


class Tracker(object):
  __metaclass__ = ABCMeta

  def __init__(self, url, port, torrent):
    self.url = url
    self.port = port
    self.torrent = torrent

  @abstractmethod
  def peers(self):
    raise NotImplemented("This method needs to be implemented")
