import requests

from .base import Tracker


class TCPTracker(Tracker):

  @property
  def peers(self):
    payload = {
        'info_hash': self.torrent.hash,
        'peer_id': self.peer_id,
        'port': 6889,
        'uploaded': 0,
        'downloaded': 0,
        'left': self.torrent['info']['length'],
        'compact': 1,
        'event': 'started',
    }
    try:
      response = requests.get(self.url, params=payload)
      print response, self.url
    except:
      print 'fail'
