print "Enter the numerator"
num=int(input())
print "Enter the denominator"
deno=int(input())
try:
   quotient=num/deno
   oFile=open('ifile','r')
except ZeroDivisionError:
   print "Enter the denominator without zero"
   deno=int(input())
   quotient=num/deno
except IOError:
   print "Now opening good file"
   oFile=open('grades.txt','r')
finally:
   print "closing all the files"
   oFile.close()

print quotient
