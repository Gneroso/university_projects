from .base import Strategy


class RarityStrategy(Strategy):

  def check_rarity(self, length):
    rarity = [{'rarity': 0, 'index': i, 'peers': []} for i in range(length)]
    for peer in self.pieces:
      for index, item in enumerate(rarity):
        item['rarity'] += int(self.pieces[peer]['bitfield'][index])
        item['peers'].append(self.pieces[peer]['peer'])
    return rarity

  def build(self):
    rarity = sorted(self.check_rarity(10),
                    key=lambda piece: piece['rarity'])

    self.start_requesting(rarity)

  def start_requesting(self, rarity):
    # piece / 16K
    BLOCK_SIZE = 2 ** 14
    piece_blocks = (self.torrent['info']['length'] / 10) / BLOCK_SIZE
    for piece in rarity:
      blocks_per_peer = piece_blocks / len(piece['peers'])
      offset = piece['index'] * (self.torrent['info']['length'] / 10)
      for index, peer in enumerate(piece['peers']):
        start = offset + index * blocks_per_peer * BLOCK_SIZE
        end = offset + (index + 1) * blocks_per_peer * BLOCK_SIZE
        block_index = 0
        while start < end:
          peer.request(piece['index'], block_index, BLOCK_SIZE)
          start += BLOCK_SIZE
          block_index += 1
