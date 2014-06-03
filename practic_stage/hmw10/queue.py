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
      if item == thing:
        found = True
      self.push(thing)

    return found
