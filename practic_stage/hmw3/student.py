class Student(object):
  def __init__(self, name, age, id, grades):
    self.name = name
    self.age = age
    self.id = id
    self.grades = grades

  def __repr__(self):
    return "< %s >" % self.name

  @property
  def total(self):
    return sum([self.grades[field] for field in self.grades])

  def __lt__(self, another_student):
    return self.total < another_student.total

  def __gt__(self, another_student):
    return self.total > another_student.total


class Students(list):
  def __init__(self, strategy):
    self.strategy = strategy

  def sort_by(self, grade):
    strategy = self.strategy(self)
    return strategy.sort_by(grade)

  def sort(self):
    strategy = self.strategy(self)
    return strategy.sort()
