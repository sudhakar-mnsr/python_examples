print "Enter grade or q to quit\n"
grade = raw_input()
while grade != 'q':
   openFile.write(grade + '\n')
   print ("Enter grade or q to quit\n")
   grade = raw_input()
   
