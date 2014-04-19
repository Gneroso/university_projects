from .base import Tracker


class TCPTracker(Tracker):
  def get_peers(self):
    print 'getting peers'
