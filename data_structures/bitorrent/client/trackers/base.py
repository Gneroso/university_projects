from abc import ABCMeta, abstractmethod


class Tracker(object):
  __metaclass__ = ABCMeta

  def __init__(self, url, port, torrent, peer_id):
    self.url = url
    self.port = port
    self.torrent = torrent
    self.peer_id = peer_id

  @abstractmethod
  def peers(self):
    raise NotImplemented("This method needs to be implemented")
