from urlparse import urlparse

from .tcp import TCPTracker
from .udp import UDPTracker


def Tracker(url, torrent, peer_id):
  parsed = urlparse(url)

  if parsed.scheme == 'udp':
    url = "%s%s" % (parsed.netloc.split(':')[0], parsed.path)
    port = parsed.port
    return UDPTracker(url, int(port), torrent, peer_id)
  elif parsed.scheme == 'http':
    return TCPTracker(url, 80, torrent, peer_id)
