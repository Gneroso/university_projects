from hashlib import sha1


class Client(object):
  def __init__(self, name):
    self.name = name

  def __hash__(self):
    return sha1(self.name).hexdigest()
