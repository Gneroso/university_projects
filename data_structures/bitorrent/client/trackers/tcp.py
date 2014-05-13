import requests

from .base import Tracker


class TCPTracker(Tracker):

  @property
  def peers(self):
    payload = {
        'info_hash': self.torrent.hash,
        'peer_id': self.peer_id,
        'port': 6888,
        'uploaded': 0,
        'downloaded': 0,
        'left': self.torrent['info']['length'],
        'compact': 1,
        'event': 'started',
        'no_peer_id': True
    }
    try:
      response = requests.get(self.url, params=payload, headers={
                                  'Content-Type': 'application/json'
                              })
      print response.content, self.url
    except:
      print 'fail'
