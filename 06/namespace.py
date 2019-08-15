import newton

def square(number):
    print "This is not from Newton !"
    return number*number

number=9
print "The square of number is " + str(square(number))
print "The square of number is " + str(newton.square(number))
