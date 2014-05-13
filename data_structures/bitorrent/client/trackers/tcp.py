import requests
import json

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
      headers = {'Content-Type': 'application/json'}
      response = requests.get(self.url, params=payload, headers=headers)
      response = json.loads(response.content)

      if response['status'] == 'success':
        return [tuple(peer.split(':')) for peer in response['message']['peers']]
      else:
        raise ValueError(response['message'])
    except Exception as e:
      raise ValueError(e.msg)
