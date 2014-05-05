from flask import Blueprint


endpoint = Blueprint('announce', __name__)


@endpoint.route('/announce')
def announce():
  return 'working'
