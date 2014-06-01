import struct

from .messages import MESSAGES


class Builder(object):
  def __call__(self, msg_type, *args):
    if msg_type in MESSAGES:
      return getattr(self, "on_%s" % msg_type)(*args)

  def on_transfer(self, *args):
    return struct.pack("!b40s40sQi", 1, *args)

  def on_pay(self, *args):
    return struct.pack("!b40s40sQi", 2, *args)

  def on_retrieve(self, *args):
    return struct.pack("!b40s40sQi", 3, *args)

  def on_receive(self, *args):
    return struct.pack("!b40s40sQi", 4, *args)

  def on_retry(self, *args):
    return struct.pack("!b", 5)

  def on_success(self, *args):
    return struct.pack("!b", 6)
