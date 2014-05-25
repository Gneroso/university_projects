import struct

from .messages import MESSAGES


class Parser(object):
  def __call__(self, message):
    length, id = struct.unpack("!bb", message[:2])
    for msg_type in MESSAGES:
      if id == MESSAGES[msg_type]:
        return msg_type, getattr(self, "on_" % msg_type)(message)
    return None

  def on_choke(self, message):
    return struct.unpack("!bb", message)

  def on_unchoke(self, message):
    return struct.unpack("!bb", message)

  def on_no_interested(self, message):
    return struct.unpack("!bb", message)

  def on_interested(self, message):
    return struct.unpack("!bb", message)

  def on_have(self, message):
    return struct.unpack("!bbi", message)

  def on_bitfield(self, message):
    return struct.unpack("!bbi", message)

  def on_request(self, message):
    return struct.unpack("!bbiii", message)

  def on_piece(self, message):
    length, id, piece_index, start = struct.unpack("!hbhh", message[:7])
    return length, id, piece_index, start, message[7:]

  def on_cancel(self, message):
    return struct.unpack("!bbiii", message)

  def on_port(self, message):
    return struct.unpack("!bbb", message)
