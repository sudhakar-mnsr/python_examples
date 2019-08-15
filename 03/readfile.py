total=0
count=0
inFile = open('grade.txt', 'r')
grade = inFile.readline()
while (grade):
   total = total + int(grade)
   count = count + 1
   grade = inFile.readline()
print ("The average is " + str(total))
