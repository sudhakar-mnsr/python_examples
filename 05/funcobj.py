def square(x):
   return x*x

sqnum = square(2)
print (sqnum)

sqnumfunc = square
sqnum2 = sqnumfunc(20)
print (sqnum2)

# Higher order function Map
# easy way to take function and apply to list
numbers = [1,2,3,4,5]
sqnum3=list(map(square, numbers))
print (sqnum3)

# lambda functions (anonymous functions)
numbers4 = [1,2,3,4,5]
square = lambda x: x*x
print (square(200000000))
cubenumbers = list(map(lambda x: x*x*x, numbers4))
print (cubenumbers)

# filter example
def even(x):
   if x%2 == 0:
     return True
   else:
     return False 
evennum = list(filter(even,numbers))
print (evennum)

# reduce example
def sum(x,y):
   return x+y
import functools
total = functools.reduce(sum,numbers)
print (total)
