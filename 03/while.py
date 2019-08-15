openFile = open("grade.txt", 'a')
print "Enter grade or q to quit\n"
grade = raw_input()
sum = 0
count = 0
while grade != 'q':
   sum = sum + int(grade)
   count = count + 1
   openFile.write(grade + '\n')
   print ("Enter grade or q to quit\n")
   grade = raw_input()
   
print ("the average grade is: " + str(sum/count))
