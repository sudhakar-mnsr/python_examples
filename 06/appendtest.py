# This test fails
numbers=[1,2,3,4,5]
numbers.append(6)
print len(numbers)
numbers[len(numbers)]=7
print numbers
