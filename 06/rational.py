class Rational:
   def __init__(self,num,deno):
       self.num=num
       self.deno=deno
       if self.deno == 0:
          raise ZeroDivisionError()
   def __str__(self):
       return str(self.num) + ' ' + str(self.deno)

try:
   r1=Rational(4,0)
except ZeroDivisionError:
   print "Please no zeros"
   r1=Rational(4,1)
print r1

