class Student(object):
  def __init__(self, name, age, id, grades):
    self.name = name
    self.age = age
    self.id = id
    self.grades = grades


class Students(list):
  def sort_by(self, grade):
    pass
