from utils import add_two_binary, substract_binary


def signed(first, second):
  if first[0] == second[0]:
    result = add_two_binary(first, second)
    if result[0] != first[0]:
      raise ValueError("Overflow")
    return result

  if first[1:] >= second[1:]:
    larger = first[1:]
    smaller = second[1:]
  else:
    larger = second[1:]
    smaller = first[1:]

  result = substract_binary(larger, smaller)
  if len(result) > 7:
    raise ValueError("Overflow")

  return larger[0] + result
