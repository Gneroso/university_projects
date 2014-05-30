from abc import ABCMeta, abstractmethod


class Strategy(object):
  __metaclass__ = ABCMeta

  def __init__(self, items):
    self.items = items

  @abstractmethod
  def sort_by(self, field, key=None):
    raise NotImplemented("Each sorting strategy has a sort method for sorting")
