class Student:
   grades=[]
   def __init__(self,name,id):
     self.name=name
     self.id=id
   def appendGrades(self,grade):
     self.grades.append(grade)
   def showGrades(self):
     grads=''
     for grade in self.grades:
         grads+=str(grade) + ' '
     return grads
   def __str__(self):
      return "Name: " + self.name + '\n' \
             "ID: " + str(self.id) + '\n' \
             "Grades:" + self.showGrades() + '\n'  
   def average(self):
      sum=0
      for grade in self.grades:
          sum+=grade
      return sum/len(self.grades)    

aStudent=Student('Sudhakar',1)
aStudent.appendGrades(99)
aStudent.appendGrades(91)
aStudent.appendGrades(9)
aStudent.appendGrades(98)
aStudent.appendGrades(100)
print aStudent.showGrades()
print aStudent
print aStudent.average()
