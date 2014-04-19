from abs import ABCMeta, abstractmethod


class Tracker(object):
  __metaclass__ = ABCMeta

  def __init__(self, url, port):
    self.url = url
    self.port = port

  @abstractmethod
  def get_peers(self):
    raise NotImplemented("This method needs to be implemented")
