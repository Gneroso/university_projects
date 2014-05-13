import struct
import socket
import time

from trackpy.vendors.redis import redis


class Torrent(object):
  def __init__(self, info_hash):
    self.info = redis.hgetall(info_hash)
    self.info_hash = info_hash

  def can_announce(self, peer_id):
    timestamp = int(redis.get("%s_%s" % (self.info_hash, peer_id)) or 0)
    if not timestamp:
      return True

    now = int(time.time())

    return False if now - timestamp > 5 * 60 else True

  def set_announce(self, peer_id):
    redis.set("%s_%s" % (self.info_hash, peer_id), int(time.time()))

  @property
  def peers(self):
    return redis.smembers('%s_peers' % self.info_hash)

  @peers.setter
  def peers(self, peer):
    redis.sadd('%s_peers' % self.info_hash, peer)

  @property
  def seeders(self):
    return self.info['seeders'] if 'seeders' in self.info else []

  @property
  def leechers(self):
    return self.info['leecher'] if 'leechers' in self.info else []
