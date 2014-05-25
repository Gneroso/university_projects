import urllib
import traceback
from random import randint

from trackers import Tracker
from torrnt import Torrent
from peer import Peer

from strategies import RarityStrategy


class Client(object):

  def __init__(self, torrent):
    self.peer_id = urllib.quote("-AZ2470-" + "".join([str(randint(0, 9))
                                                     for i in xrange(12)]))
    self.torrent = Torrent(torrent)
    self.strategy = RarityStrategy

  @property
  def strategy(self):
    return self.strategy

  @strategy.setter
  def strategy(self, strategy):
    self.strategy = strategy

  @property
  def peers(self):
    peers = []

    for url in self.torrent.urls:
      peers += Tracker(url, self.torrent, self.peer_id).peers

    return set(peers)

  def download(self):
    try:
      # TODO: create a thread pool and wait until everybody is ready
      pieces = {}
      for raw_peer in self.peers:
        peer = Peer(raw_peer[0], raw_peer[1], self.peer_id, self.torrent)
        pieces[peer] = {
            'bitfield': peer.bitfield,
            'peer': peer
        }
      self.strategy(pieces, self.torrent).build()
    except ValueError as e:
      print traceback.format_exc()
      print e
