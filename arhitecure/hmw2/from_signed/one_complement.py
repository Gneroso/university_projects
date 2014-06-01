def one_complement(signed):
  return signed[0] + ''.join(['1' if bit == '0' else '1'
                              for bit in signed[1:]])
