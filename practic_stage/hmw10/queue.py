def queue():
  _queue = []

  def pop():
    return _queue.pop()

  def push(item):
    _queue.append(item)

  def is_empty():
    return len(_queue) == 0

  return pop, push, is_empty
