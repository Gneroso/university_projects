def signed(one_complement):
  return one_complement[0] + ''.join(['1' if bit == '0' else '0'
                                      for bit in one_complement[1:]])
