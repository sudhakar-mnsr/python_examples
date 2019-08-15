name = raw_input()
print (name)
# Enter number but raw_input defaults to string
# number is read as string typecast to int

# on entering 100 the output is 100100
number = raw_input()
print (number*2)

# on entering 100 the output is 200
number = int(raw_input())
print (number*2)
