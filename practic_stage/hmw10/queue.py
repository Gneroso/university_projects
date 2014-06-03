def queue():
  _queue = []

  def pop():
    return _queue.pop()

  def push(item):
    _queue.append(item)

  def is_empty():
    return len(_queue) == 0

  return pop, push, is_empty


class Queue(object):
  def __init__(self):
    self._queue = queue

  def pop(self):
    return self._queue.pop()

  def push(self, item):
    self._queue.append(item)

  @property
  def empty(self):
    return len(self._queue) == 0

  @property
  def size(self):
    return len(self.queue)

  def load(self, data):
    for item in data:
      self.push(item)

  def __contains__(self, item):
    found = False
    initial_size = self.size

    while initial_size:
      thing = self.pop()
      if item == thing[0]:
        found = True
      self.push(thing[0])

      initial_size -= 1

    return found

  def find(self, item):
    initial_size = self.size

    while initial_size:
      thing = self.pop()
      if item == thing[0]:
        return thing
      self.push(thing)

      initial_size -= 1

    return False

  def __iter__(self):
    initial_size = self.size

    while initial_size:
      thing = self.pop()
      yield(thing)
      self.push(thing)
      initial_size -= 1

    raise StopIteration()

  def __repr__(self):
    rep = ""
    for item in self._queue:
      rep += "%s," % item
    return rep
