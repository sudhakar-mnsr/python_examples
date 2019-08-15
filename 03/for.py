numbers = [1,2,3,4,5]
tnumbers = (100,200,300,400,500)
phones = {'sudhakar':1,'krupakar':2,'latha':3}
sum =0
for i in numbers:
   sum = sum + i

print ("The total is " + str(sum))

# index into the numbers
for i in range(0,len(numbers)):
   print (numbers[i])
# index into numbers increment by n
for i in range(0,len(numbers),3):
   print (numbers[i])

# for using tuples
for i in range(0,len(tnumbers),3):
   print (tnumbers[i])

# for using dictionaries
for i in phones.keys():
   print (phones[i])

# Readng files using for 
sum = 0
count = 0
for grade in open('grade.txt'):
    count = count+1
    sum =  sum + int(grade)
print ('The average is :' + str(sum/count))    
