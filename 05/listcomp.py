numbers = range(1,101)
#for i in range(0,len(numbers)):
#   print (numbers[i] + 5)
# list comprehension is to simplify for loop as below
# the below for loop replace two lines in above for loop

numbers = range(1,101)
numbers = [grade + 5 for grade in numbers]
print (numbers)
