import hashlib
import os

from bencode import bencode


FILE_NAME = 'examples/file.txt'
CHUNKS = 10
SIZE = os.stat(FILE_NAME).st_size
HASHES = []


with open(FILE_NAME) as f:
  for i in range(CHUNKS):
    f.seek(i * (SIZE / CHUNKS))
    HASHES.append(hashlib.sha1(f.read(SIZE / CHUNKS)).digest())

torrent = {
    'announce': 'http://localhost:5000/announce',
    'announce-list': ['udp://localhost:9999'],
    'info': {
        'length': SIZE,
        'piece lenght': int(SIZE / CHUNKS),
        'pieces': ''.join(HASHES)
    }
}

with open('examples/uploads/testing.torrent', 'w') as f:
  f.write(bencode(torrent))

with open('examples/progress/testing.progress', 'w') as f:
  f.write(bencode({
      'pieces': HASHES
  }))
