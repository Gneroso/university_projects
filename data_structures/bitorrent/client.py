import hashlib
import socket
import struct
import urllib
import random
from random import randint
from urlparse import urlparse

from bencode import bdecode, bencode


with open('test.torrent') as f:
  content = f.read()
  metainfo = bdecode(content)

urls = [metainfo['announce']]
urls += [announce[0] for announce in metainfo['announce-list']]
for url in urls:
  print urlparse(url)

url = "tracker.istole.it"
port = 80
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(3)

# get connection_id
connection_id = 0x41727101980
action = 0x0
transaction_id = int(random.randrange(0, 255))
info_hash = urllib.quote(hashlib.sha1(bencode(metainfo['info'])).digest())

message = struct.pack("!q", connection_id)
message += struct.pack("!i", action)
message += struct.pack("!i", transaction_id)
sock.sendto(message, (url, port))
data, addr = sock.recvfrom(1024)
action, transaction_id, connection_id = struct.unpack(">LLQ", data)
print action

a = """
action = 0x2
message = struct.pack("!q", connection_id)
message += struct.pack("!i", action)
message += struct.pack("!i", transaction_id)
message += struct.pack("!20s", info_hash)
sock.sendto(message, (url, port))
data, addr = sock.recvfrom(1024)
data = struct.unpack(">LLLQ", data)
print data
"""

# announce
transaction_id = int(random.randrange(0, 255))
peer_id = urllib.quote("-AZ2470-" + "".join([str(randint(0, 9)) for i in xrange(12)]))
action = 0x1
left = metainfo['info']['length']
downloaded = 0x0
uploaded = 0x0
ip = 0x0
key = 0x0
event = 0x2
num_wat = -1
port = 80

args = (connection_id, action,
        transaction_id, info_hash, peer_id, downloaded, left,
        uploaded, ip, key, event, num_wat, port)
message = struct.pack("!qii20s20sqqqiIIiH", *args)
print len(message)
sock.sendto(message, (url, port))
data, addr = sock.recvfrom(2048)
print len(data)
action = struct.unpack("!iiiii", data[:20])
ip, port = struct.unpack_from("!ih", data[20:])
print socket.inet_ntoa(hex(ip)[2:].zfill(8).decode('hex'))
# scrape
action = 0x2
transaction_id = int(random.randrange(0, 255))
args = (connection_id, action,
        transaction_id, info_hash)
message = struct.pack(">qii20s", *args)
sock.sendto(message, (url, port))
while True:
  data, addr = sock.recvfrom(2048)
  print len(data)
  action = struct.unpack(">iiiii", data)
  print "noo", action
