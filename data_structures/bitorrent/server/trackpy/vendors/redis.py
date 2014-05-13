from __future__ import absolute_import

from redis import StrictRedis
from trackpy.app import get_config

config = get_config()
redis = StrictRedis.from_url(config.REDIS_URL)
