import time
import Thread

from abc import ABCMeta, abstractmethod


class Watcher(object):
  __metaclass__ = ABCMeta

  def __init__(self, data_to_watch, interval):
    self.data_to_watch = data_to_watch

  def watch(self, interval):
    thread = Thread(target=self.run, args=(self, interval,))
    thread.daemon = True
    thread.start()

  @abstractmethod
  def run(self, interval):
    raise NotImplemented("Every watcher has a watch method")


class Writer(Watcher):
  def run(self, interval):
    while True:
      with open("logs/now", "w") as f:
        f.seek(0)
        f.write(self.data_to_watch)
        f.truncate()
        time.sleep(interval)


class Caller(Watcher):
  def run(self, interval):
    while True:
      while not self.data_to_watch['booked_phone'].empty:
        ticket = self.data_to_watch['booked_phone'].pop()
        self.data_to_watch['tickets'].push(ticket)

      time.sleep(interval)
