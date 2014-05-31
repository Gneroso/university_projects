from .base import Strategy


class InsertionSort(Strategy):
  def sort_by(self, field):
    return self._sort(lambda x, y: x.grades[field] < y.grades[field])

  def sort(self):
    return self._sort(lambda x, y: x < y)

  def _sort(self, compare):
   for first_item in range(len(self.items)):
      for second_item in range(first_item + 1, len(self.items)):
        if compare(self.items[first_item], self.items[second_item]):
          aux = self.items[first_item]
          self.items[first_item] = self.items[second_item]
          self.items[second_item] = aux
