import struct


class Image(object):
  def __init__(self, path):
    self.path = path

    self.info = self._get_info()
    self.matrix = self._get_matrix()

  def _get_info(self):
    with open(self.path) as f:
      return f.read(54)

  def _get_matrix(self):
    pixels = []
    with open(self.path) as f:
      f.seek(54)
      pixel = f.read(3)
      while pixel != "" and len(pixel) == 3:
        pixels.append(struct.unpack("!bbb", pixel))
        pixel = f.read(3)
    return pixels

  def new_image(self, path, change):
    with open(path, 'w') as f:
      f.write(self.info)
      for pixel in self.matrix:
        pixel = change(pixel)
        f.write(struct.pack("!bbb", *pixel))
