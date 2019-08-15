class Shape:
   def __init__(self,xcor,ycor):
       self.xcor=xcor
       self.ycor=ycor
   def __str__(self):
      return str(self.xcor) + ' ' + str(self.ycor)
   def move(self,xcor,ycor):
       self.xcor+=xcor
       self.ycor+=ycor

class Rectangle(Shape):
    def __init__(self,xcor,ycor,width,height):
        Shape.__init__(self,xcor,ycor)
        self.width=width
        self.height=height
    def __str__(self):
        retStr=Shape.__str__(self)
        retStr+=" " + str(self.width) + " " + str(self.height)
        return retStr

aShape=Shape(10,10)
print aShape

aRectangle=Rectangle(10,10,100,100)
print aRectangle
