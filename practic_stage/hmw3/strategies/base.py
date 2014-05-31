from abc import ABCMeta, abstractmethod


class Strategy(object):
  __metaclass__ = ABCMeta

  def __init__(self, items):
    self.items = items

  @abstractmethod
  def sort_by(self, field, key=None):
    message = "Each sorting strategy has a sort_by method for sorting"
    raise NotImplemented(message)

  @abstractmethod
  def sort(self, field, key=None):
    raise NotImplemented("Each sorting strategy has a sort method for sorting")
