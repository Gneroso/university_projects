class Student(object):
  def __init__(self, name, age, id, grades, prev=None, next=None):
    self.name = name
    self.age = age
    self.id = id
    self.grades = grades

    self.prev = prev
    self.next = next

  def __repr__(self):
    return "< %s >" % self.name

  @property
  def total(self):
    return sum([self.grades[field] for field in self.grades])

  def __lt__(self, another_student):
    return self.total < another_student.total

  def __gt__(self, another_student):
    return self.total > another_student.total


class Students(object):
  def __init__(self, strategy):
    self.strategy = strategy

    self.head = None
    self.tail = None
    self.size = 0

    self.iterator_start = None

  def sort_by(self, grade):
    strategy = self.strategy(self)
    return strategy.sort_by(grade)

  def sort(self):
    strategy = self.strategy(self)
    return strategy.sort()

  def append(self, student):
    if self.head is None:
      self.head = student
      self.tail = self.head
    else:
      student.prev = self.tail
      self.tail.next = student
      self.tail = student

    self.size += 1

  def interchange(self, first_node, second_node):
    for item in self:
      if item.name == first_node.name:
        item.next = second_node.next
        item.prev = second_node.prev
        item.name = second_node.name
        item.grades = second_node.grades
        item.age = second_node.age
        break

    for item in self:
      if item.name == second_node.name:
        item.next = first_node.next
        item.prev = first_node.prev
        item.name = first_node.name
        item.grades = first_node.grades
        item.age = first_node.age
        break

  def __iter__(self):
    return StudentsIterator(self.iterator_start or self.head)


class StudentsIterator(object):
  def __init__(self, current):
    self.current = current

  def __iter__(self):
    return self

  def next(self):
    if self.current is None:
      raise StopIteration()

    result = self.current
    self.current = result.next

    return result
