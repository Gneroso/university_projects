import struct

from .messages import MESSAGES


class Parser(object):
  def __call__(self, message):
    id = struct.unpack("!b", message[:1])[0]
    for msg_type in MESSAGES:
      if id == MESSAGES[msg_type]:
        return msg_type, getattr(self, "on_%s" % msg_type)(message)
    return None

  def on_transfer(self, message):
    return struct.unpack("!b40s40sQi", message)

  def on_pay(self, message):
    return struct.unpack("!b40s40sQi", message)

  def on_receive(self, message):
    return struct.unpack("!b40s40sQi", message)

  def on_retrieve(self, message):
    return struct.unpack("!b40s40sQi", message)

  def on_retry(self, message):
    return 5

  def on_success(self, message):
    return 6
