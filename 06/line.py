class Point:
   def __init__(self,xcor,ycor):
       self.xcor=xcor
       self.ycor=ycor
   def __str__(self):
       return str(self.xcor) +','+str(self.ycor)

class Line:
   def __init__(self,p1,p2):
       self.p1=p1
       self.p2=p2
   def __str__(self):
      return str(self.p1) + '::' + str(self.p2)
p1=Point(1,1)
p2=Point(10,10)
l1=Line(p1,p2)
print l1

