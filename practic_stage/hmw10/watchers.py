import time
import Thread

from abc import ABCMeta, abstractmethod


class Watcher(object):
  __metaclass__ = ABCMeta

  def __init__(self, data_to_watch):
    self.data_to_watch = data_to_watch

  def watch(self):
    thread = Thread(target=self.run, args=(self,))
    thread.daemon = True
    thread.start()

  @abstractmethod
  def run(self):
    raise NotImplemented("Every watcher has a watch method")


class Writer(Watcher):
  def run(self):
    while True:
      with open("logs/now", "w") as f:
        f.seek(0)
        f.write(self.data_to_watch)
        f.truncate()
        time.sleep(5)


class Caller(Watcher):
  def run(self):
    print 'awesome'
