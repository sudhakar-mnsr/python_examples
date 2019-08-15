numbers = [1,2,3,4,5]
phones = {'sudhakar': 1, 'krupakar':2, 'latha': 3}
it = iter(numbers)
print (it.__next__())
print(next(it))

rfile = open('grades.txt','r')
print (next(rfile),end='')

it = iter(phones)
print (next(it))
