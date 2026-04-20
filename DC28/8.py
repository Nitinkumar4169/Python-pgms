#wap to create an inner class inside a class
class School():
  def __init__(self,name):
    self.name = name

  class Student():
    def __init__(self,roll):
      self.roll = roll

#object of school
s = School("chaman bhartiya")

#obj of student
ans = School.Student(76)
print(ans.roll)
