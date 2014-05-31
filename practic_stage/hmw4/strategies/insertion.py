from copy import deepcopy

from .base import Strategy


class InsertionSort(Strategy):
  def sort_by(self, field):
    return self._sort(lambda x, y: x.grades[field] < y.grades[field])

  def sort(self):
    return self._sort(lambda x, y: x < y)

  def _sort(self, compare):
    for first_item in self.items:
      items = deepcopy(self.items)
      items.iterator_start = first_item.next
      for second_item in items:
        if compare(first_item, second_item):
          self.items.interchange(first_item, second_item)
