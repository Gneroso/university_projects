import json

from flask import Blueprint, request

from utils.decorators import required

from .torrent import Torrent


endpoint = Blueprint('announce', __name__)


@endpoint.route('/announce', methods=['GET'])
@required('info_hash', 'peer_id', 'port', 'uploaded', 'downloaded', 'left',
          'compact', 'no_peer_id', 'event')
def announce(info_hash, peer_id, port, uploaded, downloaded, left, compact,
             no_peer_id, event):
  torrent = Torrent(info_hash)
  if not torrent.can_announce(peer_id):
    return json.dumps({
        'status': 'fail',
        'message': 'You need to wait 5 minutes to reannounce yourself'
    })

  torrent.peers = "%s:%s" % (request.remote_addr, port)
  torrent.set_announce(peer_id)

  response = {
      'status': 'success',
      'message': {
          'interval': 5 * 60,
          'complete': torrent.seeders,
          'incomplete': torrent.leechers,
          'peers': list(torrent.peers),
      }
  }
  return json.dumps(response)
