import struct

from .messages import MESSAGES


class Builder(object):
  def __call__(self, msg_type, *args):
    if msg_type in MESSAGES:
      return getattr(self, "on_%s" % msg_type)(*args)

  def on_choke(self, *args):
    return struct.pack("!bb", 1, 0)

  def on_unchoke(self, *args):
    return struct.pack("!bb", 1, 1)

  def on_no_interested(self, *args):
    return struct.pack("!bb", 1, 3)

  def on_interested(self, *args):
    return struct.pack("!bb", 1, 2)

  def on_have(self, *args):
    return struct.pack("!bbi", 5, 4, *args)

  def on_bitfield(self, *args):
    return struct.pack("!bbi", 6, 5, *args)

  def on_request(self, *args):
    return struct.pack("!bbiii", 13, 6, *args)

  def on_piece(self, piece_index, start, content):
    message = struct.pack("!bbii", 9, 7, piece_index, start)
    return message + content

  def on_cancel(self, *args):
    return struct.pack("!bbiii", *args)

  def on_port(self, *args):
    return struct.pack("!bbb", *args)
