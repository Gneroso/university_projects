from .base import Strategy


class RarityStrategy(Strategy):

  def check_rarity(self, length):
    rarity = [{'rarity': 0, 'index': i, 'peers': []} for i in range(length)]
    for peer in self.pieces:
      for index, item in enumerate(rarity):
        print self.pieces[peer]
        item['rarity'] += int(self.pieces[peer]['bitfield'][index])
        item['peers'].append(self.pieces[peer]['peer'])
    return rarity

  def build(self):
    rarity = sorted(self.check_rarity(10),
                    key=lambda piece: piece['rarity'])

    self.start_requesting(rarity)

  def start_requesting(self, rarity):
    # piece / 16K
    piece_blocks = self.torrent['info']['length'] / (2 ** 14)
    for piece in rarity:
      blocks_per_peer = len(piece['peers'])
      for index, peer in enumerate(piece['peers']):
        start = index * blocks_per_peer * piece_blocks
        end = (index + 1) * blocks_per_peer * piece_blocks
        peer.request(piece['index'], start, end)
