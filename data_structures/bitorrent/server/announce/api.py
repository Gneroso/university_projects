from flask import Blueprint

from utils.decorators import required


endpoint = Blueprint('announce', __name__)


@endpoint.route('/announce', methods=['GET'])
@required('info_hash', 'peer_id', 'port', 'uploaded', 'downloaded', 'left',
          'compact', 'no_peer_id', 'event')
def announce(info_hash, peer_id, port, uploaded, downloaded, left, compact,
             no_peer_id, event):
  return 'working'
